---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.1 Account Identification", "7.1.1.4 AccountIdentification55Choice", "7.1.1.4.3 UPIC <UPIC>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.1.4.3 UPIC <UPIC>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
Definition: Basic Bank Account Number (BBAN) - identifier used nationally by financial institutions, ie, in
individual countries, generally as part of a National Account Numbering Scheme(s), to uniquely identify
the account of a customer.
Datatype: "BBANIdentifier" on page 663
7.1.1.4.3  UPIC <UPIC>
Presence: [1..1]
Definition: Universal Payment Identification Code (UPIC) - identifier used by the New York Clearing
House to mask confidential data, such as bank accounts and bank routing numbers. UPIC numbers
remain with business customers, regardless of banking relationship changes.
Datatype: "UPICIdentifier" on page 665
7.1.1.4.4  ProprietaryAccount <PrtryAcct>
Presence: [1..1]
Definition: Account number used by financial institutions in individual countries to identify an account of
a customer, but not necessarily the bank and branch of the financial institution in which the account is
held.
ProprietaryAccount <PrtryAcct> contains the following elements (see
"SimpleIdentificationInformation2" on page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 278
7.1.2 Agreement
7.1.2.1  Agreement5
Definition: Contractual details related to the agreement between parties.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Description <Desc> [0..1] Text 225
   Date <Dt> [0..1] DateTime 226
   Currency <Ccy> [0..1] CodeSet C1 226
   ClosingType <ClsgTp> [0..1] CodeSet 226
   StartDate <StartDt> [0..1] DateTime 226
   DeliveryType <DlvryTp> [0..1] CodeSet 227
   MarginRatio <MrgnRatio> [0..1] Rate 227
7.1.2.1.1  Description <Desc>
Presence: [0..1]
Definition: Full name of the base standard agreement, annexes and amendments in place between the
principals and applicable to this deal.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 225 February 2025
```

