---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Account Link Creation Request"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.049.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P408–P414; payload P417–P439"}, {"source_id": "src-000365", "locator": "Word file/printed pages28,29"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
issue_ids: ["issue-000053"]
source_editions: ["december-2024"]
---

# Account Link Creation Request

[src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P408–P414, payload P417–P439. [reda.049.001.01](../../../../messages/reda.049.001.01/index.md).

**P408** The instructing Party wants to create a new Account Link between a Securities Account and a dedicated cash account, with default link flag set to true, with the following information:

**P409** Securities Account: SACCCSDA

**P410** Dedicated Cash Account: CASHACCOUNT

**P411** Valid From: 2015-06-01

**P412** Default Indicator: true

**P413** Collateralisation Indicator: false

**P414** Cash Settlement Indicator: false

```xml
<AcctLkCreReq>
	<MsgHdr>
		<MsgId>CREACCLINK</MsgId>
	</MsgHdr>
	<AcctLk>
		<SctiesAcct>
			<Id>SACCCSDA</Id>
			</SctiesAcct>
		<CshAcct>
			<Id>
				<Othr>
					<Id>CASHACCOUNT</Id>
				</Othr>
			</Id>
		</CshAcct>
		<VldFr>
			<Dt>2015-06-01</Dt>
		</VldFr>
		<DfltInd>true</DfltInd>
		<CollstnInd>false</CollstnInd>
		<CshSttlmInd>true</CshSttlmInd>
	</AcctLk>
</AcctLkCreReq>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word28](../../../../../../../evidence/omitted/9acb443febfdd3cc8b80d780.md), [Word29](../../../../../../../evidence/omitted/724c9bbca6f2aa6ee79f4f8a.md). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
