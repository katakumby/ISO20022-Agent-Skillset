---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.2.2.14 NearTermPositionLimit <NearTermPosLmt>"]
file_pages: [1687]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.2.14 NearTermPositionLimit <NearTermPosLmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1687 to 1687.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1687

```text
PositionLimit <PosLmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.2.2.14  NearTermPositionLimit <NearTermPosLmt>
Presence: [0..1]
Definition: Near-term position limit for the instrument.
NearTermPositionLimit <NearTermPosLmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.2.2.15  ListingDate <ListgDt>
Presence: [0..1]
Definition: Original Date/time at which the security is listed at the specific exchange or trading venue.
Datatype: "ISODate" on page 3319
28.4.2.2.2.16  RecordDate <RcrdDt>
Presence: [0..1]
Definition: Date/time at which positions are struck to note which parties are entitled to receive the
entitlement to a corporate event or vote at a meeting.
Datatype: "ISODateTime" on page 3320
28.4.2.2.2.17  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 3319
28.4.2.2.2.18  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 3327
28.4.2.2.2.19  ClassificationType <ClssfctnTp>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1687 August 2026
```

