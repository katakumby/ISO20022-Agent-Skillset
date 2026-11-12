---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.2 Message Datatypes", "4.2.2 CodeSet", "4.2.2.2 AddressType2Code"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.2.2 AddressType2Code

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
Format
pattern [A-Z]{3,3}
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
4.2.2.2  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
4.2.2.3  AdjustmentDirection1Code
Definition: Specifies whether the adjustment is added or subtracted to the total amount.
Type: CodeSet
CodeName Name Definition
ADDD Added Adjustment amount must be added to
the total amount.
SUBS Substracted Adjustment amount must be substracted
from the total amount.
4.2.2.4  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 144 December 2025
```

