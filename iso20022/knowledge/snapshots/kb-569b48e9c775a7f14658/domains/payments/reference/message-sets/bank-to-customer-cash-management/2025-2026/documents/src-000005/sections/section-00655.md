---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.4 AttendanceContext1Code"]
file_pages: [888]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.4 AttendanceContext1Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 888 to 888.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 888

```text
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
6.2.2.4  AttendanceContext1Code
Definition: Human attendance at the POI location during the transaction.
Type: CodeSet
CodeName Name Definition
ATTD Attended Attended payment, with an attendant.
SATT SemiAttended Semi-attended, including self checkout.
An attendant supervises several
payment, and could be called to help the
cardholder.
UATT Unattended Unattended payment, no attendant
present.
6.2.2.5  AuthenticationEntity1Code
Definition: Entity or object in charge of verifying the cardholder authenticity.
Type: CodeSet
CodeName Name Definition
ICCD ICC Application in the chip card (Integrated
Circuit Card), for instance an offline PIN
verification.
AGNT AuthorisedAgent Authorisation agent of the issuer.
MERC Merchant Merchant (for example signature
verification by the attendant).
6.2.2.6  AuthenticationMethod1Code
Definition: Method used to authenticate a cardholder.
Type: CodeSet
CodeName Name Definition
UKNW UnknownMethod Authentication method is performed
unknown.
BYPS Bypass Authentication bypassed by the
merchant.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
888 March 2026
```

