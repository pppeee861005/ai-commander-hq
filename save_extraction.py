import json
from pathlib import Path

chunk_result = {
    "nodes": [
        {"id": "agentic_new_city_agent_system", "label": "Agentic New City Agent System", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "three_layer_architecture", "label": "Three-Layer Architecture", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "sensing_layer_agent", "label": "Sensing Layer", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "brain_layer_agent", "label": "Brain Layer (Graphify-based)", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "execution_layer_agent", "label": "Execution Layer", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "digital_asset_gravity", "label": "Digital Asset Gravity Theory", "file_type": "rationale", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "urban_renewal_coordination", "label": "Urban Renewal Coordination", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "technical_feasibility_assessment", "label": "Technical Feasibility Assessment", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "sensing_layer_feasibility", "label": "Sensing Layer Feasibility (88%)", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "brain_layer_feasibility", "label": "Brain Layer Feasibility (100%)", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "execution_layer_feasibility", "label": "Execution Layer Feasibility (95%)", "file_type": "document", "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "phased_implementation", "label": "Phased Implementation (PHASE 0-3)", "file_type": "rationale", "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
        {"id": "risk_mitigation", "label": "Risk Mitigation Strategy", "file_type": "rationale", "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None}
    ],
    "edges": [
        {"source": "agentic_new_city_agent_system", "target": "three_layer_architecture", "relation": "implements", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "three_layer_architecture", "target": "sensing_layer_agent", "relation": "consists_of", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "three_layer_architecture", "target": "brain_layer_agent", "relation": "consists_of", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "three_layer_architecture", "target": "execution_layer_agent", "relation": "consists_of", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "brain_layer_agent", "target": "digital_asset_gravity", "relation": "rationale_for", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "agentic_new_city_agent_system", "target": "urban_renewal_coordination", "relation": "coordinates", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "agentic_new_city_agent_system", "target": "phased_implementation", "relation": "follows", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "technical_feasibility_assessment", "target": "sensing_layer_feasibility", "relation": "evaluates", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "technical_feasibility_assessment", "target": "brain_layer_feasibility", "relation": "evaluates", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "technical_feasibility_assessment", "target": "execution_layer_feasibility", "relation": "evaluates", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "sensing_layer_agent", "target": "sensing_layer_feasibility", "relation": "semantically_similar_to", "confidence": "INFERRED", "confidence_score": 0.95, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "brain_layer_agent", "target": "brain_layer_feasibility", "relation": "semantically_similar_to", "confidence": "INFERRED", "confidence_score": 0.95, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "execution_layer_agent", "target": "execution_layer_feasibility", "relation": "semantically_similar_to", "confidence": "INFERRED", "confidence_score": 0.95, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "technical_feasibility_assessment", "target": "risk_mitigation", "relation": "rationale_for", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "agentic_new_city_agent_system", "target": "risk_mitigation", "relation": "requires", "confidence": "INFERRED", "confidence_score": 0.85, "source_file": "有興趣的主題/agentic_new_city_技術可行性評估.md", "source_location": None, "weight": 1.0},
        {"source": "brain_layer_agent", "target": "urban_renewal_coordination", "relation": "enables", "confidence": "INFERRED", "confidence_score": 0.85, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "digital_asset_gravity", "target": "urban_renewal_coordination", "relation": "applies_to", "confidence": "INFERRED", "confidence_score": 0.85, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "sensing_layer_agent", "target": "brain_layer_agent", "relation": "feeds_to", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "brain_layer_agent", "target": "execution_layer_agent", "relation": "produces_decisions_for", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0},
        {"source": "execution_layer_agent", "target": "urban_renewal_coordination", "relation": "implements", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "有興趣的主題/agentic_new_city_主體規劃.md", "source_location": None, "weight": 1.0}
    ],
    "hyperedges": [
        {
            "id": "governance_system",
            "label": "Integrated Governance System",
            "nodes": ["agentic_new_city_agent_system", "urban_renewal_coordination", "technical_feasibility_assessment"],
            "relation": "coordinate",
            "confidence": "INFERRED",
            "confidence_score": 0.85,
            "source_file": "有興趣的主題/agentic_new_city_主體規劃.md"
        },
        {
            "id": "ai_intelligence_layer",
            "label": "AI Intelligence Infrastructure",
            "nodes": ["brain_layer_agent", "digital_asset_gravity", "phased_implementation"],
            "relation": "form",
            "confidence": "INFERRED",
            "confidence_score": 0.80,
            "source_file": "有興趣的主題/agentic_new_city_主體規劃.md"
        },
        {
            "id": "physical_digital_integration",
            "label": "Physical-Digital Integration",
            "nodes": ["sensing_layer_agent", "execution_layer_agent", "urban_renewal_coordination"],
            "relation": "bridge",
            "confidence": "INFERRED",
            "confidence_score": 0.85,
            "source_file": "有興趣的主題/agentic_new_city_主體規劃.md"
        }
    ],
    "input_tokens": 0,
    "output_tokens": 0
}

Path("graphify-out").mkdir(exist_ok=True)
Path("graphify-out/.graphify_chunk_1.json").write_text(
    json.dumps(chunk_result, indent=2, ensure_ascii=False)
)
print("✅ 語義提取結果已保存")
print(f"   節點: {len(chunk_result['nodes'])}")
print(f"   邊: {len(chunk_result['edges'])}")
print(f"   超邊: {len(chunk_result['hyperedges'])}")
