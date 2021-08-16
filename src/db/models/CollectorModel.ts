import { db } from "../db";

export interface ICollector {
  id?: number;
  name: string;
  phone: string;
  password: string;
}
export class Collector {
  id: number;
  name: string;
  phone: string;
  password: string;

  constructor(name: string, phone: string, password: string, id?: number) {
    this.name = name;
    this.phone = phone;
    this.password = password;
    if (id) this.id = id;
    db.collectors.mapToClass(Collector);
  }
  save() {
    return db.collectors.put(this);
  }
}

export async function addNewCollector(data: ICollector) {
  await db.transaction("rw", db.collectors, async function () {
    await db.collectors.add(
      new Collector(data.name, data.phone, data.password, data.id)
    );
  });
}

export async function getAllcollector() {
  return await db.transaction("r", db.collectors, async function () {
    let collector = await db.collectors.toArray();
    return collector;
  });
}

export async function getCollectorById(id: number) {
  return await db.collectors.get(id);
}

export async function getCollectorByName(name: string) {
  return await db.collectors
    .where("name")
    .startsWithAnyOfIgnoreCase(name)
    .toArray();
}

export async function getCollectorByPhone(phone: string) {
  return await db.collectors
    .where("phone")
    .startsWithAnyOfIgnoreCase(phone)
    .toArray();
}

export async function getCollectorByPhoneAndPassword(
  phone: string,
  password: string
) {
  return await db.collectors
    .where({ phone: phone, password: password }).first();
}

export async function updateCollector(data: ICollector) {
  return await db.collectors.put({
    id: data.id,
    name: data.name,
    phone: data.phone,
    password: data.password,
  });
}
