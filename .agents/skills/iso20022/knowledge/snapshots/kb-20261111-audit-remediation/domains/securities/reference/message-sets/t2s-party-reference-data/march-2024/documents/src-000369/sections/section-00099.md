---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>"]
file_pages: [127, 128, 129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 127 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             ValidFrom <VldFr> [1..1] DateTime 151
             ValidUntil <VldUntil> [0..1] DateTime 151
           New <New> [1..1]  151
             RestrictionType <RstrctnTp> [1..1]  152
{Or               Code <Cd> [1..1] Text 152
Or}               Proprietary <Prtry> [1..1] ± 152
             ValidFrom <VldFr> [1..1] DateTime 152
             ValidUntil <VldUntil> [0..1] DateTime 153
Or}         Other <Othr> [1..*]  153
           FieldName <FldNm> [1..1] Text 153
           OldFieldValue <OdFldVal> [1..1] Text 153
           NewFieldValue <NewFldVal> [1..1] Text 153
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 153
       InstructingUser <InstgUsr> [1..1] Text 153
       ApprovingUser <ApprvgUsr> [0..1] Text 153
Or}     BusinessError <BizErr> [1..*]  154
       Error <Err> [1..1]  154
{Or         Code <Cd> [1..1] CodeSet 154
Or}         Proprietary <Prtry> [1..1] Text 154
       Description <Desc> [0..1] Text 154
   DatePeriod <DtPrd> [0..1]  154
{Or     FromDate <FrDt> [1..1] Date 155
Or     ToDate <ToDt> [1..1] Date 155
Or     FromToDate <FrToDt> [1..1] ± 155
Or}     Date <Dt> [1..1] Date 155
   PartyIdentification <PtyId> [1..1] ± 155
10.4.2.1.1  PartyAuditTrailOrError <PtyAudtTrlOrErr>
Presence: [1..1]
Definition: Identifies the returned party reference data or error information.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
127 March 2024
```

## File page 128

```text
PartyAuditTrailOrError <PtyAudtTrlOrErr> contains one of the following
PartyAuditTrailOrError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AuditTrail <AudtTrl> [1..*]  130
     Record <Rcrd> [1..*]  133
{Or       Address <Adr> [1..1]  136
         Old <Od> [1..1] ± 136
         New <New> [1..1] ± 137
Or       ContactDetails <CtctDtls> [1..1]  138
         Old <Od> [1..1] ± 138
         New <New> [1..1] ± 139
Or       OpeningDate <OpngDt> [1..1]  140
         Old <Od> [1..1] Date 140
         New <New> [1..1] Date 140
Or       ClosingDate <ClsgDt> [1..1]  141
         Old <Od> [1..1] Date 141
         New <New> [1..1] Date 141
Or       Type <Tp> [1..1]  141
         Old <Od> [1..1]  141
{Or           Code <Cd> [1..1] CodeSet 142
Or}           Proprietary <Prtry> [1..1] Text 142
         New <New> [1..1]  142
{Or           Code <Cd> [1..1] CodeSet 142
Or}           Proprietary <Prtry> [1..1] Text 142
Or       TechnicalAddress <TechAdr> [1..1]  142
         Old <Od> [1..1]  143
{Or           BICFI <BICFI> [1..1] IdentifierSet C2 143
Or}           TechnicalAddress <TechAdr> [1..1] Text 143
         New <New> [1..1]  143
{Or           BICFI <BICFI> [1..1] IdentifierSet C2 144
Or}           TechnicalAddress <TechAdr> [1..1] Text 144
Or       MarketSpecificAttribute <MktSpcfcAttr> [1..1]  144
         Old <Od> [1..1]  144
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
128 March 2024
```

## File page 129

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Name <Nm> [1..1] Text 145
           Value <Val> [1..1] Text 145
         New <New> [1..1]  145
           Name <Nm> [1..1] Text 145
           Value <Val> [1..1] Text 145
Or       Name <Nm> [1..1]  145
         Old <Od> [1..1]  146
           ValidFrom <VldFr> [0..1] Date 146
           Name <Nm> [1..1] Text 146
           ShortName <ShrtNm> [0..1] Text 146
         New <New> [1..1]  146
           ValidFrom <VldFr> [0..1] Date 147
           Name <Nm> [1..1] Text 147
           ShortName <ShrtNm> [0..1] Text 147
Or       ResidenceType <ResTp> [1..1]  147
         Old <Od> [1..1] CodeSet 147
         New <New> [1..1] CodeSet 148
Or       LockStatus <LckSts> [1..1]  148
         Old <Od> [1..1]  148
           ValidFrom <VldFr> [0..1] Date 149
           Status <Sts> [1..1] CodeSet 149
           LockReason <LckRsn> [0..*] Text 149
         New <New> [1..1]  149
           ValidFrom <VldFr> [0..1] Date 149
           Status <Sts> [1..1] CodeSet 149
           LockReason <LckRsn> [0..*] Text 150
Or       Restriction <Rstrctn> [1..1]  150
         Old <Od> [1..1]  150
           RestrictionType <RstrctnTp> [1..1]  151
{Or             Code <Cd> [1..1] Text 151
Or}             Proprietary <Prtry> [1..1] ± 151
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
129 March 2024
```

