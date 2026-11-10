---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Account Link Status Advice — completed"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.051.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P483–P488; payload P491–P516"}, {"source_id": "src-000365", "locator": "Word file/printed pages30,31"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
issue_ids: ["issue-000053"]
source_editions: ["december-2024"]
---

# Account Link Status Advice — completed

[src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P483–P488, payload P491–P516. [reda.051.001.01](../../../../messages/reda.051.001.01/index.md).

**P483** In this case the Account Link Creation Request has been successfully executed.

**P484** Request Message ID: ACCLINKCREAT

**P485** Securities Account: SACCCSDA

**P486** Dedicated Cash Account: CASHACCOUNT

**P487** Valid From: 2015-06-01

**P488** Status. COMP

```xml
<AcctLkStsAdvc>
	<MsgHdr>
		<MsgId>ACCLINKSTATCOMP</MsgId>
		<OrgnlBizInstr>
			<Id>ACCLINKCREAT</Id>
		</OrgnlBizInstr>
	</MsgHdr>
	<AcctLkSts>
		<Sts>COMP</Sts>
	</AcctLkSts>
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
</AcctLkStsAdvc>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word30](../../../../../assets/src-000365/source-page-renders/word-page-30.png), [Word31](../../../../../assets/src-000365/source-page-renders/word-page-31.png). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
