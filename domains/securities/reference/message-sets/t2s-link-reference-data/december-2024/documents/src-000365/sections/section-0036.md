---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["Business Examples", "\tLink Creation and Maintenance", "Account Link Creation Request- reda.049.001.01"]
content_origin: "source-transcription"
---

# Account Link Creation Request- reda.049.001.01

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path Business Examples / 	Link Creation and Maintenance / Account Link Creation Request- reda.049.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P406** Account Link Creation Request- reda.049.001.01

**P407** Description

**P408** The instructing Party wants to create a new Account Link between a Securities Account and a dedicated cash account, with default link flag set to true, with the following information:

**P409** Securities Account: SACCCSDA

**P410** Dedicated Cash Account: CASHACCOUNT

**P411** Valid From: 2015-06-01

**P412** Default Indicator: true

**P413** Collateralisation Indicator: false

**P414** Cash Settlement Indicator: false

**P416** Message Instance

**P417** 																								<AcctLkCreReq>

**P418** 																									<MsgHdr>

**P419** 																										<MsgId>CREACCLINK</MsgId>

**P420** 																									</MsgHdr>

**P421** 																									<AcctLk>

**P422** 																										<SctiesAcct>

**P423** 																											<Id>SACCCSDA</Id>

**P424** 																											</SctiesAcct>

**P425** 																										<CshAcct>

**P426** 																											<Id>

**P427** 																												<Othr>

**P428** 																													<Id>CASHACCOUNT</Id>

**P429** 																												</Othr>

**P430** 																											</Id>

**P431** 																										</CshAcct>

**P432** 																										<VldFr>

**P433** 																											<Dt>2015-06-01</Dt>

**P434** 																										</VldFr>

**P435** 																										<DfltInd>true</DfltInd>

**P436** 																										<CollstnInd>false</CollstnInd>

**P437** 																										<CshSttlmInd>true</CshSttlmInd>

**P438** 																									</AcctLk>

**P439** 																								</AcctLkCreReq>

