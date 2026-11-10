---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Security CSD Link Status Advice — completed"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.047.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P326–P331; payload P334–P361"}, {"source_id": "src-000365", "locator": "Word file/printed pages25,26"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
issue_ids: ["issue-000053"]
source_editions: ["december-2024"]
---

# Security CSD Link Status Advice — completed

[src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P326–P331, payload P334–P361. [reda.047.001.01](../../../../messages/reda.047.001.01/index.md).

**P326** In this case the Security CSD Link Creation Request has been successfully executed.

**P327** Request Message ID: SECCSDINVLINKREQ

**P328** ISIN: XXABCDEFGHI1

**P329** Investor CSD: CSDAXXYYAAA

**P330** Valid From: 2015-06-01

**P331** Status. COMP

```xml
<SctyCSDLkStsAdvc>
	<MsgHdr>
		<MsgId>NONREF</MsgId>
		<OrgnlBizInstr>
			<Id> SECCSDLINCRE </Id>
		</OrgnlBizInstr>
	</MsgHdr>
	<SctyCSDLkSts>
		<Sts>COMP</Sts>
	</SctyCSDLkSts>
	<SctyCSDLkId>
		<FinInstrmId>
			<ISIN>XXABCDEFGHI1</ISIN>
		</FinInstrmId>
		<IssrInvstrCSD>
			<InvstrCSD>
				<OrgId>
					<Id>
						<AnyBIC>CSDAXXYYAAA</AnyBIC>
					</Id>
				</OrgId>
			</InvstrCSD>
		</IssrInvstrCSD>
		<VldFr>
			<Dt>2015-06-01</Dt>
		</VldFr>
	</SctyCSDLkId>
 </SctyCSDLkStsAdvc>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word25](../../../../../assets/src-000365/source-page-renders/word-page-25.png), [Word26](../../../../../assets/src-000365/source-page-renders/word-page-26.png). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
