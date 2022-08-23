import { writable } from "svelte/store";

export const isJoinRoom = writable(false);
export const isNewRoom = writable(false);
export const currentTimeLine = writable(0);
