import { useEffect, useState } from "react";
import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import {
  FaCar,
  FaExclamationTriangle,
  FaTrafficLight,
  FaVideo,
  FaFire,
  FaMapMarkedAlt,
  FaBell,
  FaShieldAlt,
} from "react-icons/fa";

import "./App.css";

function App() {
  // CHANGE 1: Added metrics state
  const [hotspots, setHotspots] = useState([]);
  const [pis, setPis] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [metrics, setMetrics] = useState({
    queue_length: 0,
    avg_speed: 0,
    delay_index: 0,
  });

  // CHANGE 2: Added /traffic-metrics fetch
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/hotspots")
      .then((res) => setHotspots(res.data))
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/pis")
      .then((res) => setPis(res.data))
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/recommendations")
      .then((res) => setRecommendations(res.data))
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/traffic-metrics")
      .then((res) => setMetrics(res.data))
      .catch(console.error);
  }, []);

  return (
    <div className="container">

      {/* ================= HERO HEADER ================= */}

      <div className="header">

        <div>
          <div className="header-tag">
            FLIPKART GRIDLOCK HACKATHON 2026
          </div>

          <h1>
            🚗 ParkPulse AI
          </h1>

          <p>
            AI-Driven Parking Intelligence System for
            Bengaluru Traffic Management
          </p>
        </div>

        <div className="header-right">

          <div className="status-badge">
            🟢 System Active
          </div>

          <div className="last-update">
            Real-Time Analytics Enabled
          </div>

        </div>

      </div>

      {/* ================= KPI CARDS ================= */}

      <div className="cards">

        <div className="card">

          <FaCar
            size={34}
            className="card-icon"
          />

          <h3>Total Violations</h3>

          <h2>298,450</h2>

          <span>
            Bengaluru Traffic Dataset
          </span>

        </div>

        <div className="card critical-card">

          <FaExclamationTriangle
            size={34}
            className="card-icon"
          />

          <h3>Critical Hotspots</h3>

          <h2>
            {
              pis.filter(
                (p) => p.Risk === "Critical"
              ).length
            }
          </h2>

          <span>
            Immediate Intervention Needed
          </span>

        </div>

        <div className="card high-card">

          <FaTrafficLight
            size={34}
            className="card-icon"
          />

          <h3>High Risk Areas</h3>

          <h2>
            {
              pis.filter(
                (p) => p.Risk === "High"
              ).length
            }
          </h2>

          <span>
            Enhanced Enforcement Zones
          </span>

        </div>

        <div className="card detection-card">

          <FaVideo
            size={34}
            className="card-icon"
          />

          <h3>AI Detection Engine</h3>

          <h2>ONLINE</h2>

          <span>
            YOLOv8 Tracking Enabled
          </span>

        </div>

        {/* CHANGE 3: Added 3 new KPI cards */}
        <div className="card">
          <h3>🚙 Queue Length</h3>
          <h2>
            {metrics.queue_length.toFixed(1)}
          </h2>
          <span>
            Vehicles in Queue
          </span>
        </div>

        <div className="card">
          <h3>⚡ Avg Speed</h3>
          <h2>
            {metrics.avg_speed.toFixed(1)}
          </h2>
          <span>
            px/sec
          </span>
        </div>

        <div className="card">
          <h3>⏳ Delay Index</h3>
          <h2>
            {metrics.delay_index.toFixed(1)}%
          </h2>
          <span>
            Congestion Impact
          </span>
        </div>

      </div>

      {/* ================= INSIGHTS ================= */}

      <div className="insights">

        <div className="insight-item">

          <FaFire />

          <span>
            Safina Plaza remains Bengaluru's
            highest-risk parking hotspot.
          </span>

        </div>

        <div className="insight-item">

          <FaBell />

          <span>
            Multiple high-risk junctions require
            proactive deployment of enforcement teams.
          </span>

        </div>

        <div className="insight-item">

          <FaShieldAlt />

          <span>
            AI surveillance can transform
            reactive enforcement into predictive action.
          </span>

        </div>

      </div>

      {/* ================= TOP HOTSPOTS CHART ================= */}

      <div className="section">

        <div className="section-header">
          <div>
            <h2>
              <FaFire className="section-icon" />
              Top Parking Hotspots
            </h2>

            <p>
              Highest congestion-inducing parking zones
              identified using historical violations.
            </p>
          </div>
        </div>

        <ResponsiveContainer
          width="100%"
          height={350}
        >
          <BarChart
            data={hotspots.slice(0, 5)}
          >
            <XAxis
              dataKey="junction_name"
              tick={false}
            />

            <YAxis />

            <Tooltip
              contentStyle={{
                borderRadius: "12px",
              }}
            />

            <Bar
              dataKey="violations"
              fill="#2874F0"
              radius={[8, 8, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>

      </div>


      {/* ================= HEATMAP ================= */}

      <div className="section">

        <div className="section-header">

          <div>

            <h2>
              <FaMapMarkedAlt className="section-icon" />
              Bengaluru Parking Heatmap
            </h2>

            <p>
              Visual representation of illegal parking
              density across Bengaluru.
            </p>

          </div>

          <div className="heatmap-badge">
            🔥 High Density Zones
          </div>

        </div>

        <iframe
          src="/parking_heatmap.html"
          title="Parking Heatmap"
          width="100%"
          height="650"
          style={{
            border: "none",
            borderRadius: "18px",
          }}
        />

      </div>


      {/* ================= HOTSPOT LEADERBOARD ================= */}

      <div className="section">

        <div className="section-header">

          <div>

            <h2>
              🏆 Top 10 Parking Hotspots
            </h2>

            <p>
              Ranked using total parking violations
              observed across Bengaluru.
            </p>

          </div>

        </div>

        <table>

          <thead>

            <tr>
              <th>Rank</th>
              <th>Junction</th>
              <th>Violations</th>
              <th>Status</th>
            </tr>

          </thead>

          <tbody>

            {hotspots
              .slice(0, 10)
              .map((h, i) => (

                <tr key={i}>

                  <td>

                    {i === 0
                      ? "🥇"
                      : i === 1
                      ? "🥈"
                      : i === 2
                      ? "🥉"
                      : `#${i + 1}`}

                  </td>

                  <td>
                    {h.junction_name}
                  </td>

                  <td>
                    {h.violations.toLocaleString()}
                  </td>

                  <td>

                    {i === 0 ? (

                      <span className="badge critical">
                        Critical
                      </span>

                    ) : i <= 3 ? (

                      <span className="badge high">
                        High
                      </span>

                    ) : (

                      <span className="badge moderate">
                        Moderate
                      </span>

                    )}

                  </td>

                </tr>

              ))}

          </tbody>

        </table>

      </div>


      {/* ================= PARKING IMPACT SCORES ================= */}

      <div className="section">

        <div className="section-header">

          <div>

            <h2>
              🚦 Parking Impact Scores
            </h2>

            <p>
              Prioritized junction risk assessment using the
              ParkPulse Impact Score (PIS).
            </p>

          </div>

        </div>

        <table>

          <thead>

            <tr>
              <th>Junction</th>
              <th>PIS</th>
              <th>Risk Level</th>
            </tr>

          </thead>

          <tbody>

            {pis.slice(0, 10).map((p, i) => (

              <tr key={i}>

                <td>
                  {p.junction_name}
                </td>

                <td>
                  {Number(p.PIS).toFixed(1)}
                </td>

                <td>

                  <span
                    className={`badge ${
                      p.Risk === "Critical"
                        ? "critical"
                        : p.Risk === "High"
                        ? "high"
                        : "moderate"
                    }`}
                  >
                    {p.Risk}
                  </span>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>


      {/* ================= RECOMMENDATIONS ================= */}

      <div className="section">

        <div className="section-header">

          <div>

            <h2>
              🚨 Recommended Actions
            </h2>

            <p>
              AI-driven interventions to reduce
              congestion caused by illegal parking.
            </p>

          </div>

        </div>

        <div className="recommendations-grid">

          {recommendations.slice(0, 5).map((r, i) => (

            <div
              className="recommendation-card"
              key={i}
            >

              <div className="recommendation-icon">
                🚨
              </div>

              <div>

                <strong>
                  Enforcement Recommendation
                </strong>

                <p>
                  {r.Recommendation}
                </p>

              </div>

            </div>

          ))}

        </div>

      </div>


      {/* ================= AI SURVEILLANCE ================= */}

      <div className="section surveillance-section">

        <div className="section-header">

          <div>

            <h2>
              🎥 AI Surveillance Feed
            </h2>

            <p>
              Illegal parking detection using
              YOLOv8 tracking and stationary
              behaviour analysis.
            </p>

          </div>

          <div className="live-pill">
            🟢 Detection Engine Online
          </div>

        </div>

        <video controls>

          <source
            src="/annotated_parking_fixed.mp4"
            type="video/mp4"
          />

          Your browser does not support
          video playback.

        </video>

        <div className="video-note">

          <strong>Demo Information:</strong>

          <p>
            Vehicles are tracked across frames.
            Prolonged stationary behaviour triggers
            illegal parking alerts and evidence
            generation.
          </p>

        </div>

      </div>


      {/* ================= FOOTER ================= */}

      <div className="footer">

        <h3>
          🚗 ParkPulse AI
        </h3>

        <p>
          Built for Flipkart Gridlock Hackathon 2026
        </p>

        <p>
          AI-Driven Parking Intelligence for
          Smarter Cities
        </p>

        <div className="footer-tags">

          <span>
            FastAPI
          </span>

          <span>
            React
          </span>

          <span>
            YOLOv8
          </span>

          <span>
            Recharts
          </span>

          <span>
            Computer Vision
          </span>

        </div>

      </div>

    </div>
  );
}

export default App;