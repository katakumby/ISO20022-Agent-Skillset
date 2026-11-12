---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.14 NearTermPositionLimit <NearTermPosLmt>"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.14 NearTermPositionLimit <NearTermPosLmt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 413

```text
PositionLimit <PosLmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.4.14  NearTermPositionLimit <NearTermPosLmt>
Presence: [0..1]
Definition: Near-term position limit for the instrument.
NearTermPositionLimit <NearTermPosLmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.4.15  ListingDate <ListgDt>
Presence: [0..1]
Definition: Original Date/time at which the security is listed at the specific exchange or trading venue.
Datatype: "ISODate" on page 529
13.1.6.4.16  RecordDate <RcrdDt>
Presence: [0..1]
Definition: Date/time at which positions are struck to note which parties are entitled to receive the
entitlement to a corporate event or vote at a meeting.
Datatype: "ISODateTime" on page 529
13.1.6.4.17  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 529
13.1.6.4.18  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 534
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 413 March 2024
```

