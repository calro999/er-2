"use client";

import { useEffect, useRef } from "react";

interface AmateurBannerProps {
  bannerId: string;
  affiliateId: string;
}

export default function AmateurBanner({ bannerId, affiliateId }: AmateurBannerProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // DMMアフィリエイトウィジェット用の描画処理
    containerRef.current.innerHTML = "";

    const ins = document.createElement("ins");
    ins.className = "widget-banner";
    containerRef.current.appendChild(ins);

    const script = document.createElement("script");
    script.className = "widget-banner-script";
    script.src = `https://widget-view.dmm.co.jp/js/banner_placement.js?affiliate_id=${affiliateId}&banner_id=${bannerId}`;
    script.async = true;
    containerRef.current.appendChild(script);
  }, [bannerId, affiliateId]);

  return (
    <div
      ref={containerRef}
      style={{ width: "300px", height: "250px" }}
      className="overflow-hidden"
    />
  );
}
