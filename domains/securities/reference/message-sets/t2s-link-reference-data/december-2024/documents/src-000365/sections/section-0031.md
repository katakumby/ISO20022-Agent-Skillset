---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["Business Examples", "\tLink Creation and Maintenance", "Security CSD Link Modification Request - reda.046.001.01"]
content_origin: "source-transcription"
---

# Security CSD Link Modification Request - reda.046.001.01

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path Business Examples / 	Link Creation and Maintenance / Security CSD Link Modification Request - reda.046.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P281** Security CSD Link Modification Request - reda.046.001.01

**P282** Description

**P283** In this example, the instructing party wants to update the end of the validity period of a Security CSD Link identified by the couple ISIN-Investor CSD:

**P284** ISIN: XXABCDEFGHI1

**P285** Investor CSD: CSDAXXYYAAA

**P286** Valid From: 2015-06-01

**P287** Valid To: 2015-12-31

**P289** Message Instance

**P290** 																								<SctyCSDLkMntncReq>

**P291** 																									<MsgHdr>

**P292** 																										<MsgId>SECCSDLINKUPD</MsgId>

**P293** 																									</MsgHdr>

**P294** 																									<SctyCSDLkId>

**P295** 																										<FinInstrmId>

**P296** 																											<ISIN>XXABCDEFGHI1</ISIN>

**P297** 																										</FinInstrmId>

**P298** 																										<IssrInvstrCSD>

**P299** 																											<InvstrCSD>

**P300** 																												<OrgId>

**P301** 																													<Id>

**P302** 																														<AnyBIC>CSDAXXYYAAA</AnyBIC>

**P303** 																													</Id>

**P304** 																												</OrgId>

**P305** 																											</InvstrCSD>

**P306** 																										</IssrInvstrCSD>

**P307** 																										<VldFr>

**P308** 																											<Dt>2015-06-01</Dt>

**P309** 																										</VldFr>

**P310** 																									</SctyCSDLkId>

**P311** 																									<Upd>

**P312** 																										<VldTo>

**P313** 																											<Dt>2015-12-31</Dt>

**P314** 																										</VldTo>

**P315** 																									</Upd>

**P316** 																								</SctyCSDLkMntncReq>

