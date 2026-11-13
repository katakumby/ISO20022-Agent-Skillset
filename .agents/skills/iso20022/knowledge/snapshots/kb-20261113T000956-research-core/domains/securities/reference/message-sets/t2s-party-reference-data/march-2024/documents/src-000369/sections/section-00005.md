---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 reda.014.001.02 PartyCreationRequestV02", "2.2 Structure"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 2.2 Structure

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 8
   Party <Pty> [1..1]  8
     PartyIdentification <PtyId> [1..1]  10
       Identification <Id> [1..1] ± 10
       ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 10
       ValidFrom <VldFr> [0..1] Date 10
     Address <Adr> [0..*] ± 10
     ContactDetails <CtctDtls> [0..*] ± 11
     OpeningDate <OpngDt> [0..1] Date 12
     ClosingDate <ClsgDt> [0..1] Date 12
     Type <Tp> [1..1]  12
{Or       Code <Cd> [1..1] CodeSet 13
Or}       Proprietary <Prtry> [1..1] Text 13
     TechnicalAddress <TechAdr> [0..*]  13
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 13
Or}       TechnicalAddress <TechAdr> [1..1] Text 13
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  14
       Name <Nm> [1..1] Text 14
       Value <Val> [1..1] Text 14
     Name <Nm> [0..1]  14
       ValidFrom <VldFr> [0..1] Date 14
       Name <Nm> [1..1] Text 14
       ShortName <ShrtNm> [0..1] Text 15
     ResidenceType <ResTp> [0..1] CodeSet 15
     LockStatus <LckSts> [0..1]  15
       ValidFrom <VldFr> [0..1] Date 15
       Status <Sts> [1..1] CodeSet 15
       LockReason <LckRsn> [0..*] Text 16
     Restriction <Rstrctn> [0..*]  16
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
7 March 2024
```

