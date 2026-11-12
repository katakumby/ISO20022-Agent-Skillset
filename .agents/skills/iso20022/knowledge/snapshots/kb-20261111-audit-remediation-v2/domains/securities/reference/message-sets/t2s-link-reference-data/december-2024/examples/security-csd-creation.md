---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Security CSD Link Creation Request"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "Business Examples; narrative P233–P242; payload P244–P279"}, {"source_id": "src-000365", "locator": "Word file/printed pages23,24"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading indentation removed; relative indentation and XML text/attribute content retained."
limitations: ["Supplied example, not invented. P229 omits BAH/document namespace wrapper; standalone XSD validity is not asserted.", "Example correlation with other source fragments is not assumed; original request identifiers and issuer/investor labels are preserved."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
issue_ids: ["issue-000053"]
source_editions: ["december-2024"]
---

# Security CSD Link Creation Request

[src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; narrative P233–P242, payload P244–P279. [reda.045.001.01](../../../../messages/reda.045.001.01/index.md).

**P233** The instructing Party wants to create a new Security CSD Link between an ISIN and its issuer CSD with the following information:

**P234** ISIN: XXABCDEFGHI1

**P235** Issuer CSD: CSDAXXYYAAA

**P236** Security Maintenance: true

**P237** Issuance Account: ISSACCT01

**P238** Primary Account Indicator: true

**P239** Issuance Account: ISSACCT02

**P240** Primary Account Indicator: false

**P241** Default Link: true

**P242** Valid From: 2015-06-01

```xml
<SctyCSDLkCreReq>
	<MsgHdr>
		<MsgId>SECCSDLINKREQ</MsgId>
	</MsgHdr>
	<SctyCSDLk>
		<FinInstrmId>
			<ISIN>XXABCDEFGHI1</ISIN>
		</FinInstrmId>
		<IssrInvstrCSD>
			<IssrCSD>
				<OrgId>
					<Id>	
						<AnyBIC>CSDAXXYYAAA</AnyBIC>
					</Id>
				</OrgId>
			</IssrCSD>
		</IssrInvstrCSD>
		<SctyMntnc>true</SctyMntnc>
		<IssncAcct>
			<IssncAcct>
				<Id>ISSACCT01</Id>
			</IssncAcct>
		<PmryAcctInd>true</PmryAcctInd>
		</IssncAcct>
		<IssncAcct>
			<IssncAcct>
				<Id>ISSACCT02</Id>
			</IssncAcct>
		<PmryAcctInd>false</PmryAcctInd>
		</IssncAcct>
		<DfltLk>true</DfltLk>
		<VldFr>
			<Dt>2015-06-01</Dt>
		</VldFr>
	</SctyCSDLk>
</SctyCSDLkCreReq>
```

Common document indentation is removed for readability; identifiers, zeros, dates, values, element labels and attributes remain as supplied. Raw paragraph extraction retains the full original indentation.

## Review evidence

Complete narrative, identifiers, numeric/boolean values, XML labels and split boundaries compared with [Word23](../../../../../../../evidence/omitted/5207cea5a2e1d767afe33dd9.md), [Word24](../../../../../../../evidence/omitted/b4da979013840767e93b7d33.md). XML fragment parses; standalone XSD validation is not claimed. Checked2026-11-09. [Unresolved correlations and narrative/XML conflicts](../example-consistency.md).
