---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Account Link Maintenance Request"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.050.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P443–P447; payload P450–P474"}, {"source_id": "src-000365", "locator": "Word file/printed pages29,30"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
source_editions: ["december-2024"]
---

# Account Link Maintenance Request

[src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P443–P447, payload P450–P474. [reda.050.001.01](../../../../messages/reda.050.001.01/index.md).

**P443** In this example, the instructing party wants to update the end of the validity period of an Account Link identified by the couple Securities Account-Dedicated Cash Account:

**P444** Securities Account: SACCCSDA

**P445** Dedicated Cash Account: CASHACCOUNT

**P446** Valid From: 2015-06-01

**P447** Valid To: 2015-07-01

```xml
<AcctLkMntncReq>
	<MsgHdr>
		<MsgId>ACCTLINKMANT</MsgId>
	</MsgHdr>
	<AcctLkId>
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
	</AcctLkId>
	<Upd>
		<VldTo>
			<Dt>2015-07-01</Dt>
		</VldTo>
	</Upd>
</AcctLkMntncReq>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word29](../../../../../../../evidence/omitted/724c9bbca6f2aa6ee79f4f8a.md), [Word30](../../../../../../../evidence/omitted/edb84c6b95b4a4c09c901396.md). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
