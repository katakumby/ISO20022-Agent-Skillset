---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Securities account position query"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P287-P289; XML P292-P316"}, {"source_id": "src-000374", "locator": "Word file/printed pages27"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000308", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.025.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Securities account position query

[src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P287-P289; XML P292-P316.

**P287** Description

**P289** In this example a T2S Actor has sent to T2S a Securities Account Position Query requesting the current day positions related to the Restriction Type “BLK1” within its securities account “1000000123”.

```xml
<SctiesAcctPosQry>
		<Stmt>
			<DtOrPrd>
				<StmtDt>
					<Dt>2025-09-12</Dt>
				</StmtDt>
			</DtOrPrd>
			<HstrcData>false</HstrcData>
		</Stmt>
		<SchCrit>
			<SfkpgAcct>
				<Acct>
					<Id>1000000123</Id>
				</Acct>
			</SfkpgAcct>
			<SubBalTp>
				<Prtry>
					<Id>BLK1</Id>
					<Issr>T2S</Issr>
					<SchmeNm>RT</SchmeNm>
				</Prtry>
			</SubBalTp>
			<RtrZeroPos>false</RtrZeroPos>
		</SchCrit>
	</SctiesAcctPosQry>
```

## Review and validation

All source example pages compared2026-11-09: [27](../../../../../assets/src-000374/source-page-renders/word-page-27.png). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
