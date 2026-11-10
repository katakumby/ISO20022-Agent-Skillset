---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.2 Structure"]
file_pages: [2293, 2294, 2295]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2293 to 2295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2293

```text
60.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyAudtTrlRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2296
     MessageIdentification <MsgId> [1..1] Text 2297
     CreationDateTime <CreDtTm> [0..1] DateTime 2297
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2297
   ReportOrError <RptOrErr> [1..1]  2297
{Or     PartyAuditTrailReport <PtyAudtTrlRpt> [1..*]  2301
       PartyAuditTrailOrError <PtyAudtTrlOrErr> [1..1]  2304
{Or         AuditTrail <AudtTrl> [1..*]  2307
           Record <Rcrd> [1..*]  2310
{Or             Address <Adr> [1..1]  2313
               Old <Od> [1..1] ± 2313
               New <New> [1..1] ± 2314
Or             ContactDetails <CtctDtls> [1..1]  2315
               Old <Od> [1..1] ± 2315
               New <New> [1..1] ± 2316
Or             OpeningDate <OpngDt> [1..1]  2317
               Old <Od> [1..1] Date 2317
               New <New> [1..1] Date 2317
Or             ClosingDate <ClsgDt> [1..1]  2318
               Old <Od> [1..1] Date 2318
               New <New> [1..1] Date 2318
Or             Type <Tp> [1..1]  2318
               Old <Od> [1..1]  2318
{Or                 Code <Cd> [1..1] CodeSet 2319
Or}                 Proprietary <Prtry> [1..1] Text 2319
               New <New> [1..1]  2319
{Or                 Code <Cd> [1..1] CodeSet 2319
Or}                 Proprietary <Prtry> [1..1] Text 2319
Or             TechnicalAddress <TechAdr> [1..1]  2319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2293 August 2026
```

## File page 2294

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Old <Od> [1..1]  2320
{Or                 BICFI <BICFI> [1..1] IdentifierSet C2 2320
Or}                 TechnicalAddress <TechAdr> [1..1] Text 2320
               New <New> [1..1]  2320
{Or                 BICFI <BICFI> [1..1] IdentifierSet C2 2321
Or}                 TechnicalAddress <TechAdr> [1..1] Text 2321
Or             MarketSpecificAttribute <MktSpcfcAttr> [1..1]  2321
               Old <Od> [1..1]  2321
                 Name <Nm> [1..1] Text 2322
                 Value <Val> [1..1] Text 2322
               New <New> [1..1]  2322
                 Name <Nm> [1..1] Text 2322
                 Value <Val> [1..1] Text 2322
Or             Name <Nm> [1..1]  2322
               Old <Od> [1..1]  2323
                 ValidFrom <VldFr> [0..1] Date 2323
                 Name <Nm> [1..1] Text 2323
                 ShortName <ShrtNm> [0..1] Text 2323
               New <New> [1..1]  2323
                 ValidFrom <VldFr> [0..1] Date 2324
                 Name <Nm> [1..1] Text 2324
                 ShortName <ShrtNm> [0..1] Text 2324
Or             ResidenceType <ResTp> [1..1]  2324
               Old <Od> [1..1] CodeSet 2324
               New <New> [1..1] CodeSet 2325
Or             LockStatus <LckSts> [1..1]  2325
               Old <Od> [1..1]  2325
                 ValidFrom <VldFr> [0..1] Date 2326
                 Status <Sts> [1..1] CodeSet 2326
                 LockReason <LckRsn> [0..*] Text 2326
               New <New> [1..1]  2326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2294 August 2026
```

## File page 2295

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 ValidFrom <VldFr> [0..1] Date 2326
                 Status <Sts> [1..1] CodeSet 2326
                 LockReason <LckRsn> [0..*] Text 2327
Or             Restriction <Rstrctn> [1..1]  2327
               Old <Od> [1..1]  2327
                 RestrictionType <RstrctnTp> [1..1]  2328
{Or                   Code <Cd> [1..1] Text 2328
Or}                   Proprietary <Prtry> [1..1] ± 2328
                 ValidFrom <VldFr> [1..1] DateTime 2328
                 ValidUntil <VldUntil> [0..1] DateTime 2328
               New <New> [1..1]  2328
                 RestrictionType <RstrctnTp> [1..1]  2329
{Or                   Code <Cd> [1..1] Text 2329
Or}                   Proprietary <Prtry> [1..1] ± 2329
                 ValidFrom <VldFr> [1..1] DateTime 2329
                 ValidUntil <VldUntil> [0..1] DateTime 2330
Or}             Other <Othr> [1..*]  2330
               FieldName <FldNm> [1..1] Text 2330
               OldFieldValue <OdFldVal> [1..1] Text 2330
               NewFieldValue <NewFldVal> [1..1] Text 2330
           OperationTimeStamp <OprTmStmp> [1..1] DateTime 2330
           InstructingUser <InstgUsr> [1..1] Text 2330
           ApprovingUser <ApprvgUsr> [0..1] Text 2330
Or}         BusinessError <BizErr> [1..*]  2331
           Error <Err> [1..1]  2331
{Or             Code <Cd> [1..1] CodeSet 2331
Or}             Proprietary <Prtry> [1..1] Text 2331
           Description <Desc> [0..1] Text 2331
       DatePeriod <DtPrd> [0..1]  2331
{Or         FromDate <FrDt> [1..1] Date 2332
Or         ToDate <ToDt> [1..1] Date 2332
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2295 August 2026
```

