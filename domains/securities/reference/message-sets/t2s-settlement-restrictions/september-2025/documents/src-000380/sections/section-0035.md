---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Business Examples", "Intra Position Movement Query (semt.028)"]
content_origin: "source-transcription"
---

# Intra Position Movement Query (semt.028)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Business Examples / Intra Position Movement Query (semt.028).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P313** Intra Position Movement Query (semt.028)

**P314** Description

**P315** A T2S participant sends to T2S an Intra Position Movement Query requesting the full details of all movements from the deliverable position ‘AWAS’ to a reserved position ‘RSV8’ relating to securities with the ISIN ‘DE0000000999’.

**P316** Message Instance

**P318** <IntraPosMvmntQry>

**P319**     <QryDef>

**P320**       <QryTp>FULL</QryTp>

**P321**       <SchCrit>

**P322**         <FinInstrmId>

**P323**           <ISIN>DE0000000999</ISIN>

**P324**         </FinInstrmId>

**P325**         <BalTp>

**P326**           <BalFr>

**P327**             <Tp>

**P328**               <Cd>AWAS</Cd>

**P329**             </Tp>

**P330**           </BalFr>

**P331**           <BalTo>

**P332**             <Tp>

**P333**               <Prtry>

**P334**                 <Id>RSV8</Id>

**P335**                 <Issr>T2S</Issr>

**P336**                 <SchmeNm>RT</SchmeNm>

**P337**               </Prtry>

**P338**             </Tp>

**P339**           </BalTo>

**P340**         </BalTp>

**P341**       </SchCrit>

**P342**     </QryDef>

**P343** </IntraPosMvmntQry>

