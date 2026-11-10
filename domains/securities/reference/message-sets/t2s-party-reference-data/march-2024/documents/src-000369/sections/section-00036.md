---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.2 Structure"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.2 Structure

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 44
   ReportOrError <RptOrErr> [1..1]  44
{Or     PartyReport <PtyRpt> [1..*]  46
       PartyIdentification <PtyId> [1..1] ± 48
       PartyOrError <PtyOrErr> [1..1]  48
{Or         SystemParty <SysPty> [1..1]  50
           PartyIdentification <PtyId> [0..1]  52
             Identification <Id> [1..1] ± 52
             ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 52
             ValidFrom <VldFr> [0..1] Date 52
           Address <Adr> [0..1] ± 52
           ContactDetails <CtctDtls> [0..*] ± 53
           OpeningDate <OpngDt> [0..1] Date 54
           ClosingDate <ClsgDt> [0..1] Date 54
           Type <Tp> [0..1]  54
{Or             Code <Cd> [1..1] CodeSet 55
Or}             Proprietary <Prtry> [1..1] Text 55
           TechnicalAddress <TechAdr> [0..*]  55
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 55
Or}             TechnicalAddress <TechAdr> [1..1] Text 55
           MarketSpecificAttribute <MktSpcfcAttr> [0..*]  56
             Name <Nm> [1..1] Text 56
             Value <Val> [1..1] Text 56
           Name <Nm> [0..1]  56
             ValidFrom <VldFr> [0..1] Date 56
             Name <Nm> [1..1] Text 56
             ShortName <ShrtNm> [0..1] Text 56
           ResidenceType <ResTp> [0..1] CodeSet 57
           LockStatus <LckSts> [0..1]  57
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
42 March 2024
```

