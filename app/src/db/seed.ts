import api from "../Api/api";
import { addNewBasti, getBastiByName } from "./models/BastiModel";
import { addNewCollector, getCollectorByPhone } from "./models/CollectorModel";
import { addNewWard, getWardByName } from "./models/WardModel";

export async function getCollectors() {
  console.log("Synchronizing Collectors...");
  let res = await api.loadCollectors();
  if (res.status === 200) {
    let collectors = res.data;
    collectors.map(async (w: any) => {
      let checkCollector = await getCollectorByPhone(w.phone);
      if (checkCollector.length === 0) {
        await addNewCollector({ name: w.name, phone: w.phone, password: w.password, id: w.id });
      }
    });
    console.log(collectors.length, " Collectors Synced.", collectors);
  }
}

export async function getWadas() {
  console.log("Synchronizing Wards...");
  let res = await api.loadWada();
  if (res.status === 200) {
    let wards = res.data;
    wards.map(async (w: any) => {
      let checkWard = await getWardByName(w.name);
      if (checkWard.length === 0) {
        await addNewWard({ name: w.name, status: w.status, id: w.id });
      }
    });
    console.log(wards.length, " Wards Synced.");
  }
}

export async function getBastis() {
  console.log("Synchronizing Basti...");
  let res = await api.loadBasti();
    if (res.status === 200) {
      let basti = res.data;
      basti.map(async (w: any) => {
        let checkWard = await getBastiByName(w.name);
        if (checkWard.length === 0) {
          await addNewBasti({ name: w.name, status: w.status, id: w.id, wardId: w.ward_id });
        }
      });
      console.log(basti.length , " Bastis Synced.")
    }
}

export async function syncDb() {
  if (window.navigator.onLine) {
    await getCollectors()
    await getWadas();
    await getBastis();
  }
}
