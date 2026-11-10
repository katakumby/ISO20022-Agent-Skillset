---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.29 ConditionallyAcceptedStatus3Choice", "66.1.45.29.2 ReasonDetails <RsnDtls>", "66.1.45.29.2.1 Reason <Rsn>", "66.1.45.29.2.1.1 Code <Cd>"]
file_pages: [5210]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.29.2.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5210 to 5210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5210

```text
Reason <Rsn> contains one of the following ConditionallyAcceptedStatusReason3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5210
Or}   Proprietary <Prtry> [1..1] ± 5210
66.1.45.29.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Conditionally accepted reason expressed as a code.
Datatype: "ConditionallyAcceptedStatusReason2Code" on page 5286
CodeName Name Definition
DOCC AwaitingDocuments Order is pending until documents are
completed and received, eg, legal
documents from the successor, legal
proceeds because of bankruptcy,
missing signature.
AWRM AwaitingRedemptionMoney Order is accepted for further processing
but the execution of the order is pending
until there are enough funds in the
account to complete the redemption.
AWSM AwaitingSubscriptionMoney Order is accepted for further processing
but the execution of the order is pending
until there is enough cash in the account
to pay the subscription.
DUPL PossibleDuplicate Order is accepted for further processing
pending the result of the investigation for
possible duplicates.
CRED TradingLimitExceeded Order is accepted for further processing
pending the extension of the trading
limit.
66.1.45.29.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Conditionally accepted reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.29.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the conditionally accepted reason.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5210 May 2026
```

