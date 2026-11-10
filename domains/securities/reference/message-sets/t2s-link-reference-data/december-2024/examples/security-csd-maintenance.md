---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Security CSD Link Modification Request"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.046.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P283–P287; payload P290–P316"}, {"source_id": "src-000365", "locator": "Word file/printed pages24,25"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
source_editions: ["december-2024"]
---

# Security CSD Link Modification Request

[src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P283–P287, payload P290–P316. [reda.046.001.01](../../../../messages/reda.046.001.01/index.md).

**P283** In this example, the instructing party wants to update the end of the validity period of a Security CSD Link identified by the couple ISIN-Investor CSD:

**P284** ISIN: XXABCDEFGHI1

**P285** Investor CSD: CSDAXXYYAAA

**P286** Valid From: 2015-06-01

**P287** Valid To: 2015-12-31

```xml
<SctyCSDLkMntncReq>
	<MsgHdr>
		<MsgId>SECCSDLINKUPD</MsgId>
	</MsgHdr>
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
	<Upd>
		<VldTo>
			<Dt>2015-12-31</Dt>
		</VldTo>
	</Upd>
</SctyCSDLkMntncReq>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word24](../../../../../assets/src-000365/source-page-renders/word-page-24.png), [Word25](../../../../../assets/src-000365/source-page-renders/word-page-25.png). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
