import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  getAllcollector,
  getCollectorByPhoneAndPassword,
} from "../db/models/CollectorModel";
import Cookies from "universal-cookie";
import { IUser } from "../db/models/UserModel";

const cookies = new Cookies();
const initialAuth = {
  name: "",
  phone: "",
  password: "",
} as IUser;
export default function VillageProfileHome() {
  const [auth, setAuth] = useState(initialAuth as IUser);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => {
    checkInCookies();
    loadAllCollectors()
  }, []);
  // async function syncDbWithServer() {
  //   if (window.navigator.onLine) {
  //     setLoading(true);
  //     syncDb();
  //     setLoading(false);
  //   }
  // }
  // async function createUser(data: IUser) {
  //   await addNewUser(data);
  // }

  // async function getUsers() {
  //   let users = await getAllUsers();
  //   console.log(users);
  // }

  // async function getById(id: number) {
  //   let user = await getUserById(id);
  //   console.log(user);
  // }

  // async function updateUserModel(data: IUser) {
  //   let user = await updateUser(data);
  //   console.log(user);
  // }

  async function loadAllCollectors() {
    let wards = await getAllcollector();
    console.log(wards);
  }

  const handleValueChance = (e: any) => {
    e.persist();
    setAuth((auth) => ({
      ...auth,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    setLoading(true);
    let collector = await getCollectorByPhoneAndPassword(
      auth.phone,
      auth.password
    );
    if (collector) {
      setAuth((auth) => ({
        ...auth,
        id: collector?.id ? collector?.id : initialAuth.id,
        name: collector?.name ? collector?.name : '',
        phone: collector?.phone ? collector?.phone : initialAuth.phone,
      }));
      setInCookies(collector);
    } else {
      setError("Phone or Password did not match!");
    }
    setLoading(false);
  };

  const checkInCookies = () => {
    let auth = cookies.get("auth");
    if (auth) {
      setAuth({ ...auth });
    }
  };
  const setInCookies = (colelctor: IUser) => {
    cookies.set("auth", colelctor);
  };
  const clearCookies = () => {
    cookies.remove("auth");
  };

  const logout = () => {
    setAuth({ ...initialAuth });
    clearCookies();
  };

  if (loading) {
    return <div className="vp-home">Loading...</div>;
  }
  if (!auth.id) {
    return (
      <div className="vp-home">
        <form method="post" onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Phone</label>
            <input
              type="number"
              placeholder="Phone No"
              name="phone"
              value={auth?.phone}
              onChange={handleValueChance}
              required
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Password"
              name="password"
              value={auth?.password}
              onChange={handleValueChance}
              required
            />
          </div>
          <p style={{ color: "red" }}>{error}</p>
          <button>Submit</button>
        </form>
      </div>
    );
  }

  return (
    <div className="vp-home">
      <div className="welcome">
        Welcome <br />
        {auth?.name}
        <p className="logout" onClick={logout}>Logout</p>
      </div>
      <Link to="/vp-app/app/add-new">Add New Household</Link>
      <Link to="/vp-app/app/pending">Pending Data</Link>
      <Link to="/vp-app/app/incomplete">Incomplete Data</Link>
    </div>
  );
}
