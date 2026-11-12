---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.3 AddressType2Code"]
file_pages: [614]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.3 AddressType2Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 614 to 614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 614

```text
Format
pattern [A-Z]{3,3}
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
7.2.2.3  AddressType2Code
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
7.2.2.4  AffirmationStatus1Code
Definition: Specifies the affirmation status of a trade.
Type: CodeSet
CodeName Name Definition
AFFI Affirmed Status of the transaction is affirmed.
NAFI Unaffirmed Status of the transaction is unaffirmed.
7.2.2.5  AllegementReason1Code
Definition: Specifies the reason why the instruction has an allegement status.
Type: CodeSet
CodeName Name Definition
ALG1 AllegementReceived Allegement has been received and no
match could be found.
7.2.2.6  Appearance1Code
Definition: Specifies the deliverability of a security.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 614 February 2025
```

