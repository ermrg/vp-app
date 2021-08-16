import React, { useEffect, useState } from "react";
import { getAllBasti, getBastiByWardId, IBasti } from "../../../db/models/BastiModel";
import { getAllWards, IWard } from "../../../db/models/WardModel";

export default function GharKoBiabarn(props: any) {
  let { data } = props;
  const [wards, setWards] = useState([] as IWard[]);
  const [bastis, setBastis] = useState([] as IBasti[]);
  useEffect(() => {
    loadAllWada();
  }, []);
  async function loadAllWada() {
    let wards = await getAllWards();
    setWards([...wards]);
  }
  const loadBastiByWadaId = async (e: any) => {
    let wardId = e.target.value;
    let bastis = await getBastiByWardId(wardId);
    setBastis([...bastis])
  };
  return (
    <div className="vp-form">
      <div className="form-group" id="1">
        <label className="label">1. Ward No</label>
        <div className="options-verical" onChange={loadBastiByWadaId}>
          {wards.map((w, key) => (
            <div className="radio" key={key}>
              <label>
                <input type="radio" value={w.id} name="ward_no" />
                {w.name}
              </label>
            </div>
          ))}
        </div>
      </div>

      <div className="form-group" id="2">
        <label className="label">2. Basti ko Naam</label>
        <div className="options-verical">
        {bastis.map((b, key) => (
            <div className="radio" key={key}>
              <label>
                <input type="radio" value={b.id} name="basti" />
                {b.name}
              </label>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
