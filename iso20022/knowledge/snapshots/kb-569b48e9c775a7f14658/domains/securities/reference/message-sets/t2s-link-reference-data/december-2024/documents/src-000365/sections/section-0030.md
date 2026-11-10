---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["Business Examples", "\tLink Creation and Maintenance", "Security CSD Link Creation Request - reda.045.001.01"]
content_origin: "source-transcription"
---

# Security CSD Link Creation Request - reda.045.001.01

Source: [src-000365](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path Business Examples / 	Link Creation and Maintenance / Security CSD Link Creation Request - reda.045.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P231** Security CSD Link Creation Request - reda.045.001.01

**P232** Description

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

**P243** Message Instance

**P244** 																								<SctyCSDLkCreReq>

**P245** 																									<MsgHdr>

**P246** 																										<MsgId>SECCSDLINKREQ</MsgId>

**P247** 																									</MsgHdr>

**P248** 																									<SctyCSDLk>

**P249** 																										<FinInstrmId>

**P250** 																											<ISIN>XXABCDEFGHI1</ISIN>

**P251** 																										</FinInstrmId>

**P252** 																										<IssrInvstrCSD>

**P253** 																											<IssrCSD>

**P254** 																												<OrgId>

**P255** 																													<Id>	

**P256** 																														<AnyBIC>CSDAXXYYAAA</AnyBIC>

**P257** 																													</Id>

**P258** 																												</OrgId>

**P259** 																											</IssrCSD>

**P260** 																										</IssrInvstrCSD>

**P261** 																										<SctyMntnc>true</SctyMntnc>

**P262** 																										<IssncAcct>

**P263** 																											<IssncAcct>

**P264** 																												<Id>ISSACCT01</Id>

**P265** 																											</IssncAcct>

**P266** 																										<PmryAcctInd>true</PmryAcctInd>

**P267** 																										</IssncAcct>

**P268** 																										<IssncAcct>

**P269** 																											<IssncAcct>

**P270** 																												<Id>ISSACCT02</Id>

**P271** 																											</IssncAcct>

**P272** 																										<PmryAcctInd>false</PmryAcctInd>

**P273** 																										</IssncAcct>

**P274** 																										<DfltLk>true</DfltLk>

**P275** 																										<VldFr>

**P276** 																											<Dt>2015-06-01</Dt>

**P277** 																										</VldFr>

**P278** 																									</SctyCSDLk>

**P279** 																								</SctyCSDLkCreReq>

**P280** 																								

