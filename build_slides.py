#!/usr/bin/env python3
"""Replace example slides in template-swiss.html with 12 UMS product slides."""
import re

# Read the template
with open('/Users/patrickxu/Desktop/UMS_PPT/ums-ppt/index.html', 'r') as f:
    content = f.read()

# 12 UMS product slides - Swiss Internationalist Style, IKB Klein Blue
new_slides = r'''<!-- ============================================================
     UMS · Unified Management System · Product Introduction
     Swiss Internationalist Style · IKB Klein Blue
     12 Slides · 8+ different S-numbers
     ============================================================ -->

<!-- 01 / 12 · Cover · IKB Full Screen + ASCII Breathing -->
<section class="slide accent" data-animate="hero" data-layout="SWISS-COVER-ASCII">
  <div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="chrome-min">
      <div class="l">UMS · Unified Management System</div>
      <div class="r">UROVO · 01 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">PRODUCT INTRODUCTION</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(11.6vw,19vh);line-height:.94;letter-spacing:-.025em;color:#fff">UMS<br/><span style="font-style:italic;font-weight:300">统一管理平台</span></h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div data-anim="lead" class="lead" style="max-width:52ch;color:rgba(255,255,255,.86);font-weight:300">All-in-one enterprise device management platform — deploy, manage, and secure every device from a single console.</div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">UROVO · Product Team · 2026</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">→ swipe / arrow keys</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 02 / 12 · S03 Split Statement · The Elevator Pitch -->
<section class="slide" data-animate="split-statement" data-layout="S03">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">VISION · What UMS Solves</div>
      <div class="r">02 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;justify-content:center">
      <div style="display:flex;flex-direction:column;gap:1.4vh;margin-bottom:5vh">
        <div class="t-meta">WHY UMS</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(7vw,12vh);line-height:1.02;letter-spacing:-.03em">One Platform.<br/>Total <span style="color:var(--accent)">Control</span>.</h2>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;border-top:1px solid var(--border-subtle);padding-top:3vh">
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(15px,1.3vw);line-height:1.6;color:var(--text-secondary)">Enterprises deploy hundreds or thousands of mobile devices across locations. Without centralized management, IT teams drown in manual setup, inconsistent configurations, and security gaps.</div>
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(15px,1.3vw);line-height:1.6;color:var(--text-primary)">UMS puts every device under one unified console — <strong>application deployment, device configuration, content distribution, remote support, and security policy</strong> — all from a single pane of glass.</div>
      </div>
    </div>
  </div>
</section>

<!-- 03 / 12 · S17 System Diagram · Three-Layer Architecture -->
<section class="slide" data-animate="stack-build" data-layout="S17">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">ARCHITECTURE · Functional Ecosystem</div>
      <div class="r">03 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">THREE PILLARS</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(6.4vw,11.2vh);line-height:1;letter-spacing:-.025em">MAM · MDM · MCM</h2>
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(14px,1.1vw);line-height:1.5;color:var(--text-secondary);max-width:60ch">Three interdependent layers covering every aspect of enterprise mobility management.</div>
      </div>
      <div data-anim="up" class="stack-row" style="margin-top:3vh">
        <div class="stack-block b-accent">
          <div class="layer-nb">LAYER 01</div>
          <i data-lucide="smartphone" style="width:2.6vw;height:2.6vw;stroke-width:1.4;margin:1.6vh 0;color:var(--accent-on)"></i>
          <div class="layer-ttl">App Management</div>
          <div class="layer-desc">App Store · Silent Install · Version Control · App Whitelist · Kiosk Mode · Auto-start · Grayscale Release</div>
          <div class="layer-tag">MAM</div>
        </div>
        <div class="stack-block b-grey">
          <div class="layer-nb">LAYER 02</div>
          <i data-lucide="monitor" style="width:2.6vw;height:2.6vw;stroke-width:1.4;margin:1.6vh 0;color:var(--ink)"></i>
          <div class="layer-ttl">Device Control</div>
          <div class="layer-desc">Remote Desktop · Geofencing · WiFi Config · System Customization · Permission Control · Device Restore</div>
          <div class="layer-tag">MDM</div>
        </div>
        <div class="stack-block b-ink">
          <div class="layer-nb">LAYER 03</div>
          <i data-lucide="file-text" style="width:2.6vw;height:2.6vw;stroke-width:1.4;margin:1.6vh 0;color:var(--paper)"></i>
          <div class="layer-ttl">Content & Data</div>
          <div class="layer-desc">File Distribution · News Push · Remote Wipe · TLS Encryption · 24h Backup · Data Center Analytics</div>
          <div class="layer-tag">MCM</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 04 / 12 · S19 Four Cards · Core Capabilities -->
<section class="slide" data-animate="grid-reveal" data-layout="S19">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">CAPABILITIES · Core Platform Modules</div>
      <div class="r">04 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:5vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div style="height:2px;background:var(--accent);width:80px;margin-bottom:1vh"></div>
        <div class="t-meta">FOUR MODULES</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(6.4vw,11.2vh);line-height:1.05;letter-spacing:-.025em">四大核心能力</h2>
      </div>
      <div data-anim="up" style="display:grid;grid-template-columns:repeat(4,1fr);gap:2vw">
        <div style="display:flex;flex-direction:column;gap:1.6vh;padding-top:2vh;border-top:2px solid var(--accent)">
          <div class="t-meta" style="color:var(--accent)">01 · APP STORE</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:min(4vw,7vh);line-height:1;letter-spacing:-.02em;color:var(--text-primary)">应用商店</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.9vw);line-height:1.6;color:var(--text-secondary);font-weight:300">Upload, publish, and manage enterprise apps. Silent install, grayscale release, version control, and app whitelist — all from one console.</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1.6vh;padding-top:2vh;border-top:2px solid var(--border-subtle)">
          <div class="t-meta">02 · REMOTE CONTROL</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:min(4vw,7vh);line-height:1;letter-spacing:-.02em;color:var(--text-primary)">远程管控</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.9vw);line-height:1.6;color:var(--text-secondary);font-weight:300">Push configurations, freeze/unfreeze devices, send files, extract logs, reboot remotely. Full control without physical access.</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1.6vh;padding-top:2vh;border-top:2px solid var(--border-subtle)">
          <div class="t-meta">03 · GROUP MGMT</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:min(4vw,7vh);line-height:1;letter-spacing:-.02em;color:var(--text-primary)">分组管理</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.9vw);line-height:1.6;color:var(--text-secondary);font-weight:300">Organize devices by department, region, or function. Batch operations, group-based app publishing, and hierarchical subgroup support.</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1.6vh;padding-top:2vh;border-top:2px solid var(--border-subtle)">
          <div class="t-meta">04 · DATA CENTER</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:min(4vw,7vh);line-height:1;letter-spacing:-.02em;color:var(--text-primary)">数据中心</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.9vw);line-height:1.6;color:var(--text-secondary);font-weight:300">Real-time device map, traffic analytics, app inventory, device lifecycle tracking, abnormal status alerts. Exportable reports.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 05 / 12 · S22 Image Hero · Dashboard Overview -->
<section class="slide light" data-animate="image-hero" data-layout="S22">
  <div class="canvas-card" style="padding:0;display:flex;flex-direction:column;overflow:hidden">
    <div data-anim="img" style="position:relative;flex:0 0 60%;overflow:hidden;background:var(--grey-1)">
      <img src="../ums-photos/image-ums-dashboard-overview.png" alt="UMS Dashboard Overview" loading="eager" data-image-slot="s22-hero-21x9"
           style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain;object-position:center center">
      <div class="chrome-min" style="position:absolute;top:0;left:0;right:0;color:rgba(255,255,255,.9);padding:5.6vh 5vw 0;mix-blend-mode:difference">
        <div class="l">EVIDENCE · Platform Dashboard</div>
        <div class="r">05 / 12</div>
      </div>
    </div>
    <div data-anim="kpi" class="image-hero-body">
      <div style="max-width:48ch;font-family:var(--sans),var(--sans-zh);font-size:max(15px,1.3vw);line-height:1.55;font-weight:300;color:var(--text-primary);letter-spacing:-.005em">
        The UMS Dashboard delivers a real-time operational overview: online device count, abnormal status alerts, device map, and traffic analytics — all at a glance.
      </div>
      <div class="image-hero-stats" style="gap:4vw">
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Real-time</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em">100%</div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">Online device visibility with instant status refresh</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Abnormal Alerts</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em">6<span style="font-size:.36em;font-weight:300;opacity:.6;margin-left:.08em">types</span></div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">Low battery, offline, disabled — proactive alerts with drill-down</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Device Map</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em;color:var(--accent)">GPS</div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">Geographic distribution with zoom, search, and geofencing</p></div>
      </div>
    </div>
  </div>
</section>

<!-- 06 / 12 · S11 Horizontal Timeline · Device Lifecycle -->
<section class="slide" data-animate="timeline-walk" data-layout="S11">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">LIFECYCLE · Full Device Management</div>
      <div class="r">06 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">7-STAGE JOURNEY</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(6.4vw,11.2vh);line-height:1;letter-spacing:-.025em">全生命周期管理</h2>
      </div>
      <div data-anim="up" class="timeline-h" style="margin-top:4vh">
        <div class="tl-row" style="grid-template-columns:repeat(7,1fr)">
          <div class="th-node up"><div class="dot"></div><div class="label"><span class="yr">Step 01</span><span class="name">Register</span><span class="desc">Device enrollment</span></div></div>
          <div class="th-node down accent"><div class="dot"></div><div class="label"><span class="yr">Step 02</span><span class="name">Provision</span><span class="desc">Group & bind</span></div></div>
          <div class="th-node up"><div class="dot"></div><div class="label"><span class="yr">Step 03</span><span class="name">Deploy</span><span class="desc">Apps & config</span></div></div>
          <div class="th-node down"><div class="dot"></div><div class="label"><span class="yr">Step 04</span><span class="name">Monitor</span><span class="desc">Status & alerts</span></div></div>
          <div class="th-node up accent"><div class="dot"></div><div class="label"><span class="yr">Step 05</span><span class="name">Secure</span><span class="desc">Policies & lock</span></div></div>
          <div class="th-node down"><div class="dot"></div><div class="label"><span class="yr">Step 06</span><span class="name">Support</span><span class="desc">Remote assist</span></div></div>
          <div class="th-node up"><div class="dot"></div><div class="label"><span class="yr">Step 07</span><span class="name">Recycle</span><span class="desc">Wipe & reuse</span></div></div>
        </div>
      </div>
      <div style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.95vw);color:var(--text-helper);font-weight:300;margin-top:3vh;max-width:60ch;border-top:1px solid var(--border-subtle);padding-top:2vh">
        From registration to recycling, UMS covers every stage. A device leaving one cycle marks the start of another — remote factory reset ensures secure transition.
      </div>
    </div>
  </div>
</section>

<!-- 07 / 12 · S08 Duo Compare · Before vs After UMS -->
<section class="slide" data-animate="duo-mirror" data-layout="S08">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">CONTRAST · The UMS Difference</div>
      <div class="r">07 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">BEFORE & AFTER</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(7vw,12vh);line-height:1.02;letter-spacing:-.025em">Without UMS vs With UMS</h2>
      </div>
      <div data-anim="up" class="duo-compare" style="margin-top:4vh">
        <div class="col">
          <div class="col-tag"><span class="num" style="border-color:var(--grey-3);color:var(--grey-3)">Before</span> Manual Chaos</div>
          <div class="col-ttl" style="font-size:min(3vw,5.5vh);color:var(--grey-3)">逐台操作</div>
          <div class="col-desc">IT staff manually configure each device. Apps installed one by one. No visibility into device health. Security policies inconsistent.</div>
          <ul class="col-list">
            <li>No centralized dashboard</li>
            <li>Manual app installation per device</li>
            <li>Cannot enforce security policies</li>
            <li>No remote troubleshooting</li>
          </ul>
        </div>
        <div class="vrule"></div>
        <div class="col accent">
          <div class="col-tag"><span class="num" style="color:var(--accent);border-color:var(--accent)">After</span> Automated Precision</div>
          <div class="col-ttl" style="font-size:min(3vw,5.5vh);color:var(--accent)">一键管控</div>
          <div class="col-desc">One console for thousands of devices. Batch deploy apps in seconds. Real-time monitoring with alerts. Uniform security across fleet.</div>
          <ul class="col-list">
            <li>Single-pane dashboard for all devices</li>
            <li>Silent batch installation in seconds</li>
            <li>Whitelist, kiosk mode, geofencing</li>
            <li>Awesun-based remote desktop support</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 08 / 12 · S22 Image Hero · Remote Support -->
<section class="slide light" data-animate="image-hero" data-layout="S22">
  <div class="canvas-card" style="padding:0;display:flex;flex-direction:column;overflow:hidden">
    <div data-anim="img" style="position:relative;flex:0 0 60%;overflow:hidden;background:var(--grey-1)">
      <img src="../ums-photos/image-ums-remote-support.png" alt="UMS Remote Support" loading="lazy" data-image-slot="s22-hero-21x9"
           style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain;object-position:center center">
      <div class="chrome-min" style="position:absolute;top:0;left:0;right:0;color:rgba(255,255,255,.9);padding:5.6vh 5vw 0;mix-blend-mode:difference">
        <div class="l">EVIDENCE · Remote Desktop & Support</div>
        <div class="r">08 / 12</div>
      </div>
    </div>
    <div data-anim="kpi" class="image-hero-body">
      <div style="max-width:48ch;font-family:var(--sans),var(--sans-zh);font-size:max(15px,1.3vw);line-height:1.55;font-weight:300;color:var(--text-primary);letter-spacing:-.005em">
        Built on Awesun technology, UMS Remote Desktop enables instant screen mirroring and remote control — troubleshoot, guide, and operate devices without physical access.
      </div>
      <div class="image-hero-stats" style="gap:4vw">
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Remote Control</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em">Awesun</div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">View and operate device screens in real time</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Batch Ops</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em">10<span style="font-size:.36em;font-weight:300;opacity:.6;margin-left:.08em">+ types</span></div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">Freeze, unfreeze, restart, shutdown, ring, file push, message</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">Speed</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4.6vw,7.6vh);line-height:.95;letter-spacing:-.04em;color:var(--accent)">MQTT</div><div style="height:1px;background:var(--border-subtle);margin-top:auto"></div><p class="body-sm">Real-time push via MQTT + HTTP polling fallback</p></div>
      </div>
    </div>
  </div>
</section>

<!-- 09 / 12 · S06 KPI Tower · Business Value Metrics -->
<section class="slide" data-animate="measure-up" data-layout="S06">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">METRICS · Quantifiable Business Value</div>
      <div class="r">09 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:4vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">MEASURABLE IMPACT</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(6.4vw,11.2vh);line-height:1.05;letter-spacing:-.025em">UMS 为企业带来的价值</h2>
      </div>
      <div data-anim="up" class="bar-towers" style="margin-top:3vh">
        <div class="bar-tower">
          <div class="cap"><i data-lucide="trending-down" style="width:1.6vw;height:1.6vw;stroke-width:1.4"></i></div>
          <div class="body-block h-4 b-accent">
            <div class="lbl">Cost Reduction</div>
            <div class="nb"><span style="font-size:.36em;font-weight:300;opacity:.7;margin-right:.08em">↓</span>90<span class="unit">%</span></div>
            <div class="sub">Human & time cost reduction in device management</div>
          </div>
        </div>
        <div class="bar-tower">
          <div class="cap"><i data-lucide="wifi" style="width:1.6vw;height:1.6vw;stroke-width:1.4"></i></div>
          <div class="body-block h-3">
            <div class="lbl">Real-time</div>
            <div class="nb">MQTT<span class="unit">push</span></div>
            <div class="sub">Instant task delivery + HTTP fallback</div>
          </div>
        </div>
        <div class="bar-tower">
          <div class="cap"><i data-lucide="zap" style="width:1.6vw;height:1.6vw;stroke-width:1.4"></i></div>
          <div class="body-block h-2">
            <div class="lbl">Deploy Speed</div>
            <div class="nb">Instant<span class="unit">batch</span></div>
            <div class="sub">Silent install to thousands of devices in one push</div>
          </div>
        </div>
        <div class="bar-tower">
          <div class="cap"><i data-lucide="shield" style="width:1.6vw;height:1.6vw;stroke-width:1.4"></i></div>
          <div class="body-block h-1">
            <div class="lbl">Data Safety</div>
            <div class="nb">24<span class="unit">h backup</span></div>
            <div class="sub">TLS encryption + daily cloud backup + remote wipe</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 10 / 12 · S13 Three Forces · Deployment Options -->
<section class="slide" data-animate="three-forces" data-layout="S13">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">DEPLOYMENT · Flexible Infrastructure</div>
      <div class="r">10 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:4vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">THREE DEPLOYMENT MODES</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(6.4vw,11.2vh);line-height:1.05;letter-spacing:-.025em">三种部署方式</h2>
      </div>
      <div data-anim="up" style="display:grid;grid-template-columns:5fr 7fr;gap:3vw;flex:1">
        <div style="background:var(--ink);color:var(--paper);padding:4vh 2.4vw;display:flex;flex-direction:column;justify-content:space-between">
          <div>
            <div class="t-meta" style="color:rgba(255,255,255,.6);margin-bottom:2vh">DEPLOY YOUR WAY</div>
            <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5.2vw,9vh);line-height:1.03;letter-spacing:-.02em;color:#fff">Choose the<br/>right <span style="color:var(--accent-bright)">fit</span>.</h3>
          </div>
          <div class="t-meta" style="color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.15);padding-top:2vh">Public cloud · Private server · Free trial</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1.6vh">
          <div class="card-fill" style="padding:2.4vh 1.8vw;display:flex;flex-direction:column;gap:1.2vh">
            <div style="display:flex;align-items:baseline;gap:1.2vw">
              <span style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9vh);line-height:.9;color:var(--accent)">01</span>
              <div>
                <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(17px,1.6vw);line-height:1.2;color:var(--text-primary)">Public Cloud</div>
                <div style="font-family:var(--sans),var(--sans-zh);font-size:max(11px,.88vw);line-height:1.5;color:var(--text-secondary);font-weight:300;margin-top:.4vh">Standard SaaS deployment. Instant onboarding via uhomeov.urovo.com. 3G/4G/5G/Wi-Fi connectivity.</div>
              </div>
            </div>
          </div>
          <div class="card-fill" style="padding:2.4vh 1.8vw;display:flex;flex-direction:column;gap:1.2vh">
            <div style="display:flex;align-items:baseline;gap:1.2vw">
              <span style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9vh);line-height:.9;color:var(--text-primary)">02</span>
              <div>
                <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(17px,1.6vw);line-height:1.2;color:var(--text-primary)">Private Deployment</div>
                <div style="font-family:var(--sans),var(--sans-zh);font-size:max(11px,.88vw);line-height:1.5;color:var(--text-secondary);font-weight:300;margin-top:.4vh">On-premise installation within enterprise intranet. Data stays inside firewall. Supports OTA firmware upgrade (UTMS).</div>
              </div>
            </div>
          </div>
          <div class="card-fill" style="padding:2.4vh 1.8vw;display:flex;flex-direction:column;gap:1.2vh">
            <div style="display:flex;align-items:baseline;gap:1.2vw">
              <span style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9vh);line-height:.9;color:var(--text-primary)">03</span>
              <div>
                <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(17px,1.6vw);line-height:1.2;color:var(--text-primary)">Free Trial</div>
                <div style="font-family:var(--sans),var(--sans-zh);font-size:max(11px,.88vw);line-height:1.5;color:var(--text-secondary);font-weight:300;margin-top:.4vh">Experience standard UMS features at no cost before committing. Full platform evaluation with no obligation.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 11 / 12 · S15 Image Matrix · Customer Cases -->
<section class="slide" data-animate="matrix-fill" data-layout="S15">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">CASES · Deployed Across Industries</div>
      <div class="r">11 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.4vh">
        <div class="t-meta">TRUSTED BY ENTERPRISES</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5.8vw,10.2vh);line-height:1.05;letter-spacing:-.025em">千行百业 · 广泛落地</h2>
      </div>
      <div data-anim="up" style="display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(2,1fr);gap:1.2vh 1vw;flex:1;align-content:center">
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="store" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Retail</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">POS · Kiosk</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="package" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Logistics</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Warehouse · Delivery</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="credit-card" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Finance</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Payment · Security</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="building-2" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Government</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Field service</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="truck" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Transport</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Fleet mgmt</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="stethoscope" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Healthcare</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Patient data</div>
        </div>
        <div class="card-fill" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="factory" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em">Manufacturing</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:var(--text-helper);margin-top:.4vh">Production line</div>
        </div>
        <div class="card-accent" style="padding:2vh 1.2vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;min-height:12vh">
          <i data-lucide="globe" style="width:2vw;height:2vw;stroke-width:1.3;margin-bottom:1vh;color:var(--accent-on)"></i>
          <div style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(14px,1.1vw);line-height:1.2;letter-spacing:-.01em;color:var(--accent-on)">And more</div>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(10px,.7vw);line-height:1.4;color:rgba(255,255,255,.7);margin-top:.4vh">Hospitality · Education</div>
        </div>
      </div>
      <div data-anim="up" style="border-top:1px solid var(--border-subtle);padding-top:2vh;display:flex;align-items:baseline;gap:1.2vw">
        <div style="font-family:var(--sans);font-weight:200;font-size:min(6.4vw,11vh);line-height:.9;color:var(--accent)">8+</div>
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(14px,1.1vw);line-height:1.5;color:var(--text-secondary)">industries served · From retail POS to warehouse logistics,<br/>UMS adapts to every enterprise mobility scenario</div>
      </div>
    </div>
  </div>
</section>

<!-- 12 / 12 · SWISS-CLOSING-ASCII · Closing Manifesto -->
<section class="slide split" data-animate="split-statement" data-layout="SWISS-CLOSING-ASCII">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1">
          <div class="l">12 / 12</div>
          <div class="r">CLOSING</div>
        </div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em;margin-bottom:1.6vh">CONCLUSION</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(8vw,14vh);line-height:.94;letter-spacing:-.025em;font-weight:200;color:#fff">UMS<br/><span style="font-style:italic;font-weight:300">Unified</span> Mobility.</h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(13px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:300;max-width:36ch;margin-top:1.4vh">从应用分发到设备退役，一个平台覆盖设备全生命周期。安全、高效、可扩展。</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.62)">UROVO · Product Team</div>
          <div class="t-meta" style="color:rgba(255,255,255,.62)">2026.06</div>
        </div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min">
          <div class="l">TAKEAWAYS</div>
          <div class="r">03 POINTS</div>
        </div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--text-primary)">01</div>
            <div>
              <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--text-primary);margin-bottom:1vh">All-in-One Platform</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.92vw);line-height:1.6;color:var(--text-secondary);font-weight:300">MAM + MDM + MCM, three pillars unified under one console. No fragmented tools, no blind spots.</p>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--text-primary)">02</div>
            <div>
              <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--text-primary);margin-bottom:1vh">Enterprise-Grade Security</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.92vw);line-height:1.6;color:var(--text-secondary);font-weight:300">TLS encrypted transmission, 24-hour cloud backup, remote data wipe. Your data stays protected at all times.</p>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle);border-bottom:2px solid var(--accent)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--accent)">03</div>
            <div>
              <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--accent);margin-bottom:1vh">Flexible Deployment</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.92vw);line-height:1.6;color:var(--text-secondary);font-weight:300">Public cloud, private deployment, or free trial — choose the model that fits your organization's needs.</p>
            </div>
          </div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">→ 完 · UMS — Your Ultimate Mobility Solution</div>
      </div>
    </div>
  </div>
</section>
'''

# Find and replace: from first example comment to last </section> before </div>
old_start = '<!-- ============ 示例:第 1 页 · Hero Cover · IKB 满屏 + ASCII 呼吸场(默认推荐) ============'
old_end_pattern = '</section>\n\n</div>'

# Find the closing </section> before </div>
idx_old_start = content.find(old_start)
idx_old_end = content.find(old_end_pattern, idx_old_start)

if idx_old_start == -1 or idx_old_end == -1:
    print("ERROR: Could not find slide section boundaries")
    # Try alternative pattern
    idx_old_start = content.find('<section class="slide accent" data-animate="hero">')
    idx_old_end = content.rfind('</section>', 0, content.find('</div>\n\n<div id="nav">'))
    if idx_old_start == -1 or idx_old_end == -1:
        print("ERROR: Alternative pattern also failed")
        exit(1)
    idx_old_end += len('</section>')

# Build new content
new_content = content[:idx_old_start] + new_slides + '\n\n' + content[idx_old_end + len(old_end_pattern) - len('</section>\n\n</div>'):]

# But wait - the old_end_pattern includes '</section>\n\n</div>' but we want to keep </div>
# Let's take a different approach: find the two <section> tags that are the example slides
# and replace everything between (and including) them.

# More precise: find the first <section> that belongs to examples and the last </section> of examples
idx_first_example = content.find('<section class="slide accent" data-animate="hero">')
# The last example </section> is the one right before </div>\n\n<div id="nav">
idx_div_nav = content.find('</div>\n\n<div id="nav">')
# Find the last </section> before </div>
search_end = content.rfind('</section>', 0, idx_div_nav)
if idx_first_example == -1 or search_end == -1:
    print(f"ERROR: idx_first={idx_first_example}, search_end={search_end}")
    exit(1)

# The old content to replace includes the first <section> through the last </section>
old_content = content[idx_first_example:search_end + len('</section>')]

# Build the final file
final = content[:idx_first_example] + new_slides + content[search_end + len('</section>'):]

with open('/Users/patrickxu/Desktop/UMS_PPT/ums-ppt/index.html', 'w') as f:
    f.write(final)

print("SUCCESS: 12 UMS slides built into index.html")
print(f"File size: {len(final)} bytes")
