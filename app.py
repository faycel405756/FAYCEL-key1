export async function GET() {
  const res = await fetch(
    "https://sieuthidora.io.vn/br1/hma.php?step=1",
    { redirect: "follow", cache: "no-store" }
  );

  const finalUrl = new URL(res.url);
  const key = finalUrl.searchParams.get("key");

  return new Response(key ?? "NO_KEY", {
    headers: {
      "Content-Type": "text/plain",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET",
    },
  });
}
