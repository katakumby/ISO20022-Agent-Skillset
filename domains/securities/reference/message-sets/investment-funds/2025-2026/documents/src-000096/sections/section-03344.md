---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.3 ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn>", "66.1.24.4.3.2 InvestorProfileValidation <InvstrPrflVldtn>", "66.1.24.4.3.2.14 KnowYourCustomerDatabaseCheck <KnowYourCstmrDBChck>"]
file_pages: [4585]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.3.2.14 KnowYourCustomerDatabaseCheck <KnowYourCstmrDBChck>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4585 to 4585.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4585

```text
Definition: Specifies the type of due diligence checks carried out on the investor or account owner. For
definitions of ordinary, simple and enhanced know your customer checks, local market regulations
should be consulted.
KnowYourCustomerCheckType <KnowYourCstmrChckTp> contains one of the following elements
(see "KYCCheckType1Choice" on page 5042 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5042
Or}   Proprietary <Prtry> [1..1] ± 5042
66.1.24.4.3.2.14  KnowYourCustomerDatabaseCheck <KnowYourCstmrDBChck>
Presence: [0..1]
Definition: Specifies whether a customer has been checked in a Know Your Customer (KYC) database.
KnowYourCustomerDatabaseCheck <KnowYourCstmrDBChck> contains the following elements
(see "DataBaseCheck1" on page 5013 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DatabaseCheck <DBChck> [1..1] Indicator 5013
   Identification <Id> [1..1] Text 5013
66.1.24.4.4  OwnershipBeneficiaryRate <OwnrshBnfcryRate>
Presence: [0..1]
Definition: Percentage of ownership or of beneficial ownership of the shares/units in the account. All
subsequent subscriptions or purchases and or redemptions or sells will be allocated using the same
percentage.
Impacted by: C25 "OwnershipBeneficiaryRateRule"
OwnershipBeneficiaryRate <OwnrshBnfcryRate> contains the following elements (see
"OwnershipBeneficiaryRate1" on page 5018 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 5018
   Fraction <Frctn> [0..1] Text 5018
Constraints
• OwnershipBeneficiaryRateRule
Either Rate or Fraction must be present. Both may be present.
66.1.24.4.5  ClientIdentification <ClntId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4585 May 2026
```

