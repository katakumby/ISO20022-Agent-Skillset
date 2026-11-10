---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Position Query (semt.025)"]
content_origin: "source-transcription"
---

# Securities Account Position Query (semt.025)

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Business Examples / Securities Account Position Query (semt.025).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P286** Securities Account Position Query (semt.025)

**P287** Description

**P289** In this example a T2S Actor has sent to T2S a Securities Account Position Query requesting the current day positions related to the Restriction Type “BLK1” within its securities account “1000000123”.

**P290** Message Instance

**P292** <SctiesAcctPosQry>

**P293** 		<Stmt>

**P294** 			<DtOrPrd>

**P295** 				<StmtDt>

**P296** 					<Dt>2025-09-12</Dt>

**P297** 				</StmtDt>

**P298** 			</DtOrPrd>

**P299** 			<HstrcData>false</HstrcData>

**P300** 		</Stmt>

**P301** 		<SchCrit>

**P302** 			<SfkpgAcct>

**P303** 				<Acct>

**P304** 					<Id>1000000123</Id>

**P305** 				</Acct>

**P306** 			</SfkpgAcct>

**P307** 			<SubBalTp>

**P308** 				<Prtry>

**P309** 					<Id>BLK1</Id>

**P310** 					<Issr>T2S</Issr>

**P311** 					<SchmeNm>RT</SchmeNm>

**P312** 				</Prtry>

**P313** 			</SubBalTp>

**P314** 			<RtrZeroPos>false</RtrZeroPos>

**P315** 		</SchCrit>

**P316** 	</SctiesAcctPosQry>

**P317**   


