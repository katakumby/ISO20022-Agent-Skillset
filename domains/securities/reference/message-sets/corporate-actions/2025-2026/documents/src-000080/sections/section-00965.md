---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.55 DeliveryReceiptType2Code"]
file_pages: [1207]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.55 DeliveryReceiptType2Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1207 to 1207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1207

```text
16.2.2.55  DeliveryReceiptType2Code
Definition: Specifies how the transaction is to be settled.
Type: CodeSet
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
16.2.2.56  DistributionType3Code
Definition: Specifies whether the proceeds of the event will be distributed on a rolling basis rather than
on a specific date.
Type: CodeSet
CodeName Name Definition
FINL Final Final payment.
INTE Interim Interim payment.
ONGO Ongoing Event is ongoing for acceptance on an
unsolicited basis.
ROLL RollingBasis Event will have a number of acceptance
and payment dates until further
announcement by the Issuer or its agent.
16.2.2.57  DividendRateType1Code
Definition: Specifies the type of dividend rate.
Type: CodeSet
CodeName Name Definition
TXBL TaxablePortion Rate relating to the underlying security
for which tax is charged.
16.2.2.58  DutchAuctionType1Code
Definition: Specifies the type of Dutch auction.
Type: CodeSet
CodeName Name Definition
MDFD Modified All instructions are accepted at the same
price (issuer bid).
UNMD Unmodified All instructions are accepted at the
instructed price (offering bid).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1207 February 2026
```

