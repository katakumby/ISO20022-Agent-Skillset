---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["34 reda.014.001.02 PartyCreationRequestV02", "34.2 Structure"]
file_pages: [2044]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 34.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2044 to 2044.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2044

```text
34.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2045
   Party <Pty> [1..1]  2045
     PartyIdentification <PtyId> [1..1]  2047
       Identification <Id> [1..1] ± 2047
       ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2047
       ValidFrom <VldFr> [0..1] Date 2047
     Address <Adr> [0..*] ± 2047
     ContactDetails <CtctDtls> [0..*] ± 2048
     OpeningDate <OpngDt> [0..1] Date 2049
     ClosingDate <ClsgDt> [0..1] Date 2049
     Type <Tp> [1..1]  2049
{Or       Code <Cd> [1..1] CodeSet 2050
Or}       Proprietary <Prtry> [1..1] Text 2050
     TechnicalAddress <TechAdr> [0..*]  2050
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 2050
Or}       TechnicalAddress <TechAdr> [1..1] Text 2050
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2051
       Name <Nm> [1..1] Text 2051
       Value <Val> [1..1] Text 2051
     Name <Nm> [0..1]  2051
       ValidFrom <VldFr> [0..1] Date 2051
       Name <Nm> [1..1] Text 2051
       ShortName <ShrtNm> [0..1] Text 2052
     ResidenceType <ResTp> [0..1] CodeSet 2052
     LockStatus <LckSts> [0..1]  2052
       ValidFrom <VldFr> [0..1] Date 2052
       Status <Sts> [1..1] CodeSet 2052
       LockReason <LckRsn> [0..*] Text 2053
     Restriction <Rstrctn> [0..*]  2053
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2044 August 2026
```

