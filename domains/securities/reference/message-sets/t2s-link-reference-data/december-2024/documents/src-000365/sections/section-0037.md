---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["Business Examples", "\tLink Creation and Maintenance", "Account Link Maintenance Request - reda.050.001.01"]
content_origin: "source-transcription"
---

# Account Link Maintenance Request - reda.050.001.01

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path Business Examples / 	Link Creation and Maintenance / Account Link Maintenance Request - reda.050.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P441** Account Link Maintenance Request - reda.050.001.01

**P442** Description

**P443** In this example, the instructing party wants to update the end of the validity period of an Account Link identified by the couple Securities Account-Dedicated Cash Account:

**P444** Securities Account: SACCCSDA

**P445** Dedicated Cash Account: CASHACCOUNT

**P446** Valid From: 2015-06-01

**P447** Valid To: 2015-07-01

**P449** Message Instance

**P450** 																								<AcctLkMntncReq>

**P451** 																									<MsgHdr>

**P452** 																										<MsgId>ACCTLINKMANT</MsgId>

**P453** 																									</MsgHdr>

**P454** 																									<AcctLkId>

**P455** 																										<SctiesAcct>

**P456** 																											<Id>SACCCSDA</Id>

**P457** 																										</SctiesAcct>

**P458** 																										<CshAcct>

**P459** 																											<Id>

**P460** 																												<Othr>

**P461** 																													<Id>CASHACCOUNT</Id>

**P462** 																												</Othr>

**P463** 																											</Id>

**P464** 																										</CshAcct>

**P465** 																										<VldFr>

**P466** 																											<Dt>2015-06-01</Dt>

**P467** 																										</VldFr>

**P468** 																									</AcctLkId>

**P469** 																									<Upd>

**P470** 																										<VldTo>

**P471** 																											<Dt>2015-07-01</Dt>

**P472** 																										</VldTo>

**P473** 																									</Upd>

**P474** 																								</AcctLkMntncReq>

