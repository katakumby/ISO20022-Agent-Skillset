---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Business Examples", "Securities Settlement Transaction Query (semt.026)"]
content_origin: "source-transcription"
---

# Securities Settlement Transaction Query (semt.026)

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Business Examples / Securities Settlement Transaction Query (semt.026).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P319** Securities Settlement Transaction Query (semt.026)

**P320** The Securities Settlement Transaction Query message covers the following T2S message usages:

**P322** Query Type example: Settlement Instruction Query

**P323** Description

**P324** In this example a T2S Actor has sent to T2S a Settlement Instruction Query requesting all settlement instructions where the securities account is ‘1000000123’ and the settlement quantity is greater than or equal to 50000 units and less than or equal to 60000 units (as per a range of valid quantity values).

**P326** Message Instance

**P328** <SctiesSttlmTxQry>

**P329**     <QryDef>

**P330**       <QryTp>INST</QryTp>

**P331**       <SchCrit>

**P332**         <SfkpgAcct>

**P333**           <Id>1000000123</Id>

**P334**         </SfkpgAcct>

**P335**         <SttlmQty>

**P336**           <Qty>

**P337**             <Unit>

**P338**               <FrToQty>

**P339**                 <FrQty>

**P340**                   <Bdry>50000</Bdry>

**P341**                   <Incl>true</Incl>

**P342**                 </FrQty>

**P343**                 <ToQty>

**P344**                   <Bdry>60000</Bdry>

**P345**                   <Incl>true</Incl>

**P346**                 </ToQty>

**P347**               </FrToQty> 

**P348**             </Unit>

**P349**           </Qty>

**P350**         </SttlmQty>

**P351**       </SchCrit>

**P352**     </QryDef>

**P353**  </SctiesSttlmTxQry>

**P354**   


**P356** Query Type Example: Settlement Instruction Current Status Query

**P357** Description 

**P358** In this example a T2S actor has sent to T2S a Settlement Instruction Current Status Query requesting all high priority “High [0003]” settlement instructions for securities account ‘1000000123’ where the settlement status is pending.

**P360** Message Instance

**P362** <SctiesSttlmTxQry>

**P363**     <QryDef>

**P364**       <QryTp>STTS</QryTp>

**P365**       <SchCrit>

**P366**         <Sts>

**P367**           <Tp>

**P368**             <SttlmSts>

**P369**               <Cd>PEND</Cd>

**P370**             </SttlmSts>

**P371**           </Tp>

**P372**         </Sts>

**P373**         <Prty>

**P374**           <Nmrc>0003</Nmrc>

**P375**         </Prty>

**P376**         <SfkpgAcct>

**P377**           <Id>1000000123</Id>

**P378**         </SfkpgAcct>

**P379**       </SchCrit>

**P380**     </QryDef>

**P381** </SctiesSttlmTxQry>

**P382**   


**P384** Query Type Example: Settlement Instruction Status Audit Trail Query

**P385** Description

**P386** In this example a T2S actor has sent to T2S a Settlement Instruction Status Audit Query requesting settlement instructions for a specific T2S securities account ‘1000000123’ that were matched on or before the 25th of September 2025.

**P388** Message Instance

**P390** <SctiesSttlmTxQry>

**P391**     <QryDef>

**P392**       <QryTp>STPD</QryTp>

**P393**       <SchCrit>

**P394**         <Sts>

**P395**           <Tp>

**P396**             <MtchgSts>

**P397**               <Cd>MACH</Cd>

**P398**             </MtchgSts>

**P399**           </Tp>

**P400**           <DtPrd>

**P401**             <Dt>

**P402**               <ToDt>2025-09-25</ToDt>

**P403**             </Dt>

**P404**           </DtPrd>

**P405**         </Sts>

**P406**         <SfkpgAcct>

**P407**           <Id>1000000123</Id>

**P408**         </SfkpgAcct>

**P409**       </SchCrit>

**P410**     </QryDef>

**P411** </SctiesSttlmTxQry>

**P412**   


