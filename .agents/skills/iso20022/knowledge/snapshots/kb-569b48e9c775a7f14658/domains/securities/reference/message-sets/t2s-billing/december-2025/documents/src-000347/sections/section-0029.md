---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["Business Examples", "Billing", "camt.076.001.01 CumulativeBillingDataQuery"]
content_origin: "source-transcription"
---

# camt.076.001.01 CumulativeBillingDataQuery

Source: [src-000347](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Locator: heading path Business Examples / Billing / camt.076.001.01 CumulativeBillingDataQuery.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P175** camt.076.001.01 CumulativeBillingDataQuery

**P176** Description

**P177** The CumulativeBillingDataQuery enables the sender to request the billing data of an invoice, which consists of the aggregated information for a specified period for each service item.

**P178** Message Instance

**P179** <BllgRptReq>

**P180**         <MsgHdr>

**P181**             <MsgId>NONREF</MsgId>

**P182**             <ReqTp>

**P183**                 <Prtry>

**P184**                     <Id>CUMU</Id>

**P185**                 </Prtry>

**P186**             </ReqTp>

**P187**         </MsgHdr>

**P188**         <SchCrit>

**P189**             <Svc>

**P190**                 <SysId>

**P191**                     <MktInfrstrctrId>

**P192**                         <Prtry>T2</Prtry>

**P193**                     </MktInfrstrctrId>

**P194**                 </SysId>

**P195**             </Svc>

**P196**             <BllgId>BILLINGIDABC00001</BllgId>

**P197**             <BllgPrd>

**P198**                 <FrDt>2019-01-01</FrDt>

**P199**                 <ToDt>2019-01-31</ToDt>

**P200**             </BllgPrd>

**P201**             <RspnsblPtyId>

**P202**                 <Id>

**P203**                     <AnyBIC>BITAITRRXXX</AnyBIC>

**P204**                 </Id>

**P205**             </RspnsblPtyId>

**P206**         </SchCrit>

**P207** </BllgRptReq>

