---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Security CSD Link Status Advice — queued"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.047.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P365–P367; payload P370–P380"}, {"source_id": "src-000365", "locator": "Word file/printed pages27"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
issue_ids: ["issue-000053"]
source_editions: ["december-2024"]
---

# Security CSD Link Status Advice — queued

[src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P365–P367, payload P370–P380. [reda.047.001.01](../../../../messages/reda.047.001.01/index.md).

**P365** This example describes the case in which the Security CSD Link Creation Request has been delayed.  

**P366** Request Message ID: SECCSDLINCRE

**P367** Status: QUED

```xml
<SctyCSDLkStsAdvc>
	<MsgHdr>
		<MsgId>NONREF</MsgId>
		<OrgnlBizInstr>
			<Id> SECCSDLINCRE </Id>
		</OrgnlBizInstr>
	</MsgHdr>
	<SctyCSDLkSts>
		<Sts>QUED</Sts>
	</SctyCSDLkSts>
</SctyCSDLkStsAdvc>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word27](../../../../../../../evidence/omitted/1ec545b1edccbd14aad5cc8c.md). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
