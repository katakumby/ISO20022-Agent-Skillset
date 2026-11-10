---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 PartyReport <PtyRpt>", "5.4.2.1.2 PartyOrError <PtyOrErr>", "5.4.2.1.2.1 SystemParty <SysPty>"]
file_pages: [50, 51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.4.2.1.2.1 SystemParty <SysPty>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 50 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}   BusinessError <BizErr> [1..*]  58
     Error <Err> [1..1]  58
{Or       Code <Cd> [1..1] CodeSet 59
Or}       Proprietary <Prtry> [1..1] Text 59
     Description <Desc> [0..1] Text 59
5.4.2.1.2.1  SystemParty <SysPty>
Presence: [1..1]
Definition: Specifications of a party defined within a system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
50 March 2024
```

## File page 51

```text
SystemParty <SysPty> contains the following SystemParty6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [0..1]  52
     Identification <Id> [1..1] ± 52
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 52
     ValidFrom <VldFr> [0..1] Date 52
   Address <Adr> [0..1] ± 52
   ContactDetails <CtctDtls> [0..*] ± 53
   OpeningDate <OpngDt> [0..1] Date 54
   ClosingDate <ClsgDt> [0..1] Date 54
   Type <Tp> [0..1]  54
{Or     Code <Cd> [1..1] CodeSet 55
Or}     Proprietary <Prtry> [1..1] Text 55
   TechnicalAddress <TechAdr> [0..*]  55
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 55
Or}     TechnicalAddress <TechAdr> [1..1] Text 55
   MarketSpecificAttribute <MktSpcfcAttr> [0..*]  56
     Name <Nm> [1..1] Text 56
     Value <Val> [1..1] Text 56
   Name <Nm> [0..1]  56
     ValidFrom <VldFr> [0..1] Date 56
     Name <Nm> [1..1] Text 56
     ShortName <ShrtNm> [0..1] Text 56
   ResidenceType <ResTp> [0..1] CodeSet 57
   LockStatus <LckSts> [0..1]  57
     ValidFrom <VldFr> [0..1] Date 57
     Status <Sts> [1..1] CodeSet 57
     LockReason <LckRsn> [0..*] Text 57
   Restriction <Rstrctn> [0..*]  58
     ValidFrom <VldFr> [1..1] DateTime 58
     ValidTo <VldTo> [0..1] DateTime 58
     Type <Tp> [1..1] Text 58
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
51 March 2024
```

