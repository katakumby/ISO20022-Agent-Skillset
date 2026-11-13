---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.20 Issuance <Issnc>", "13.1.6.2.20.6 IssuerOrganisation <IssrOrg>", "13.1.6.2.20.6.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.20.6.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
PrimaryCommunicationAddress <PmryComAdr> contains the following elements (see
"CommunicationAddress3" on page 491 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 491
   Phone <Phne> [0..1] Text 491
   Mobile <Mob> [0..1] Text 492
   FaxNumber <FaxNb> [0..1] Text 492
   TelexAddress <TlxAdr> [0..1] Text 492
   URLAddress <URLAdr> [0..1] Text 492
13.1.6.2.20.6.11  SecondaryCommunicationAddress <ScndryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 491 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 491
   Phone <Phne> [0..1] Text 491
   Mobile <Mob> [0..1] Text 492
   FaxNumber <FaxNb> [0..1] Text 492
   TelexAddress <TlxAdr> [0..1] Text 492
   URLAddress <URLAdr> [0..1] Text 492
13.1.6.2.20.7  IssueNominalAmount <IsseNmnlAmt>
Presence: [0..1]
Definition: Total original amount or quantity published.
IssueNominalAmount <IsseNmnlAmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.20.8  FullIssuedAmount <FullIssdAmt>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 266 March 2024
```

