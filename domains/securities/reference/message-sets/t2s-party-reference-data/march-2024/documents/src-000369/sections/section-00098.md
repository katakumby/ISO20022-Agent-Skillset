---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>"]
file_pages: [124, 125, 126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 124 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Description <Desc> [0..1] Text 156
10.4.2.1  PartyAuditTrailReport <PtyAudtTrlRpt>
Presence: [1..*]
Definition: Report information about party reference data.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
124 March 2024
```

## File page 125

```text
PartyAuditTrailReport <PtyAudtTrlRpt> contains the following PartyAuditTrailReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyAuditTrailOrError <PtyAudtTrlOrErr> [1..1]  127
{Or     AuditTrail <AudtTrl> [1..*]  130
       Record <Rcrd> [1..*]  133
{Or         Address <Adr> [1..1]  136
           Old <Od> [1..1] ± 136
           New <New> [1..1] ± 137
Or         ContactDetails <CtctDtls> [1..1]  138
           Old <Od> [1..1] ± 138
           New <New> [1..1] ± 139
Or         OpeningDate <OpngDt> [1..1]  140
           Old <Od> [1..1] Date 140
           New <New> [1..1] Date 140
Or         ClosingDate <ClsgDt> [1..1]  141
           Old <Od> [1..1] Date 141
           New <New> [1..1] Date 141
Or         Type <Tp> [1..1]  141
           Old <Od> [1..1]  141
{Or             Code <Cd> [1..1] CodeSet 142
Or}             Proprietary <Prtry> [1..1] Text 142
           New <New> [1..1]  142
{Or             Code <Cd> [1..1] CodeSet 142
Or}             Proprietary <Prtry> [1..1] Text 142
Or         TechnicalAddress <TechAdr> [1..1]  142
           Old <Od> [1..1]  143
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 143
Or}             TechnicalAddress <TechAdr> [1..1] Text 143
           New <New> [1..1]  143
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 144
Or}             TechnicalAddress <TechAdr> [1..1] Text 144
Or         MarketSpecificAttribute <MktSpcfcAttr> [1..1]  144
           Old <Od> [1..1]  144
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
125 March 2024
```

## File page 126

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Name <Nm> [1..1] Text 145
             Value <Val> [1..1] Text 145
           New <New> [1..1]  145
             Name <Nm> [1..1] Text 145
             Value <Val> [1..1] Text 145
Or         Name <Nm> [1..1]  145
           Old <Od> [1..1]  146
             ValidFrom <VldFr> [0..1] Date 146
             Name <Nm> [1..1] Text 146
             ShortName <ShrtNm> [0..1] Text 146
           New <New> [1..1]  146
             ValidFrom <VldFr> [0..1] Date 147
             Name <Nm> [1..1] Text 147
             ShortName <ShrtNm> [0..1] Text 147
Or         ResidenceType <ResTp> [1..1]  147
           Old <Od> [1..1] CodeSet 147
           New <New> [1..1] CodeSet 148
Or         LockStatus <LckSts> [1..1]  148
           Old <Od> [1..1]  148
             ValidFrom <VldFr> [0..1] Date 149
             Status <Sts> [1..1] CodeSet 149
             LockReason <LckRsn> [0..*] Text 149
           New <New> [1..1]  149
             ValidFrom <VldFr> [0..1] Date 149
             Status <Sts> [1..1] CodeSet 149
             LockReason <LckRsn> [0..*] Text 150
Or         Restriction <Rstrctn> [1..1]  150
           Old <Od> [1..1]  150
             RestrictionType <RstrctnTp> [1..1]  151
{Or               Code <Cd> [1..1] Text 151
Or}               Proprietary <Prtry> [1..1] ± 151
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
126 March 2024
```

