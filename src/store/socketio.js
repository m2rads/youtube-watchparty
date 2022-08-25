import { io } from "socket.io-client";

let URL = "smth";

export const socket = io(URL, { autoConnect: false });
