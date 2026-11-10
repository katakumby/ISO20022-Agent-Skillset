---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.105 PreferredContactMethod1Code"]
file_pages: [1230]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.105 PreferredContactMethod1Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1230 to 1230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1230

```text
CodeName Name Definition
LACK LackOfSecurities Insufficient financial instruments in your
account.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
MCER MissingCertification Awaiting receipt of adequate
certification.
MTAX MissingTaxRate Tax rate is missing.
OTHR Other Other. See Narrative.
FULL PendingBeneficiaryOwnerDetails Pending receipt of beneficiary owner
details.
PENR PendingReceipt Instruction is pending receipt of
securities, for example, from a purchase
or loan.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
SNAV SystemNotAvailable System is not available. Instruction is
sent outside of business hours.
CERT WrongCertificatesNumbers Certificate number error.
16.2.2.105  PreferredContactMethod1Code
Definition: Preferred method used to reach the individual contact within an organisation.
Type: CodeSet
CodeName Name Definition
LETT Letter Preferred method used to reach the
contact is per letter.
MAIL Email Preferred method used to reach the
contact is per email.
PHON Phone Preferred method used to reach the
contact is per phone.
FAXX Fax Preferred method used to reach the
contact is per fax.
CELL MobileOrCellPhone Preferred method used to reach the
contact is per mobile or cell phone.
16.2.2.106  PriceCalculationMethod1Code
Definition: Standard code to specify the method applied for the calculation of the price.
Type: CodeSet
CodeName Name Definition
VWAP VolumeWeightedAveragePrice The price is based on a volume-
weighted average price which is a ratio
of the cumulative share price to the
cumulative volume traded over a given
time period.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1230 February 2026
```

