<script>
  import JoinRoom from "../lib/JoinRoom.svelte";
  import NewRoom from "../lib/NewRoom.svelte";
  import { socket } from "../store/socketio";

  socket.on("connected", () => {
    console.log("connected");
  });

  socket.on("disconnected", () => {
    console.log("disconnected");
  });

  let showNewRoom = false;
  let showJoinRoom = false;

  function toggleNewRoom() {
    showJoinRoom = false;
    if (showNewRoom) {
      showNewRoom = false;
    } else {
      showNewRoom = true;
    }
  }

  function toggleJoinRoom() {
    showNewRoom = false;
    if (showJoinRoom) {
      showJoinRoom = false;
    } else {
      showJoinRoom = true;
    }
  }
</script>

<div class="home">
  <div class="container">
    <div class="card">
      <div class="room-container">
        <div class="join">
          <button class="button-room" on:click={toggleJoinRoom}
            >Join Room</button
          >

          {#if showJoinRoom}
            <hr />
            <NewRoom />
          {/if}
        </div>
        <div class="new">
          <button class="button-room" on:click={toggleNewRoom}
            >Create New Room</button
          >
          {#if showNewRoom}
            <hr />
            <NewRoom />
          {/if}
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .container .card {
    margin: 0 auto;
    position: relative;
    width: 320px;
    height: 450px;
    border-radius: 20px;
    background-color: #efebe9;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    overflow: hidden;
    text-align: center;
  }

  .card div {
    margin: 30px auto;
  }

  .room-container {
    display: grid;
    align-items: center;
    justify-content: center;
    align-content: center;
    min-height: 60%;
    min-height: 40vh;
  }

  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    align-content: center;
    min-height: 100%;
    min-height: 100vh;
  }

  /* CSS */
  .button-room {
    background-color: #4e342e;
    border: 1px solid transparent;
    border-radius: 0.75rem;
    box-sizing: border-box;
    color: #ffffff;
    cursor: pointer;
    flex: 0 0 auto;
    font-family: "Inter var", ui-sans-serif, system-ui, -apple-system, system-ui,
      "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif,
      "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol",
      "Noto Color Emoji";
    font-size: 1.125rem;
    font-weight: 600;
    line-height: 1.5rem;
    padding: 0.75rem 1.2rem;
    text-align: center;
    text-decoration: none #6b7280 solid;
    transition-duration: 0.2s;
    transition-property: background-color, border-color, color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    width: auto;
  }

  .button-room:hover {
    background-color: #374151;
  }

  .button-room:focus {
    box-shadow: none;
    outline: 2px solid transparent;
    outline-offset: 2px;
  }

  @media (min-width: 768px) {
    .button-room {
      padding: 0.75rem 1.5rem;
    }
  }
</style>
