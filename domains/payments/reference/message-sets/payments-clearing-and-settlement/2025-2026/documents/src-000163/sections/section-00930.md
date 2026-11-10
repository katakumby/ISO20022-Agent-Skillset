---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.3 CodeSet", "10.2.3.3 AddressType2Code"]
file_pages: [1225]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.3.3 AddressType2Code

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1225 to 1225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1225

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
10.2.3.3  AddressType2Code
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
10.2.3.4  Authorisation1Code
Definition: Specifies the level of approval depending on a number of factors, including payment type,
threshold amount or local country or operations practice.
Type: CodeSet
CodeName Name Definition
AUTH PreAuthorisedFile Indicates a file has been pre authorised
or approved within the originating
customer environment and no further
approval is required.
FDET FileLevelAuthorisationDetails Indicates that a file requires additional
file level approval, with the ability to view
both the payment information block and
supporting customer credit transaction
detail.
FSUM FileLevelAuthorisationSummary Indicates that a file requires additional
file level approval, with the ability to view
only the payment information block level
information.
ILEV InstructionLevelAuthorisation Indicates that a file requires all customer
transactions to be authorised or
approved.
10.2.3.5  ChargeBearerType1Code
Definition: Specifies which party(ies) will pay charges due for processing of the instruction.
Type: CodeSet
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1225 March 2026
```

