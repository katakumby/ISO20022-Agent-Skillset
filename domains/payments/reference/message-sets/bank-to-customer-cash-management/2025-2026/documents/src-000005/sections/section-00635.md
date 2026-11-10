---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Payment Type"]
file_pages: [868]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17 Payment Type

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 868 to 868.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 868

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 872 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 872
   Name <Nm> [0..1] Text 872
   PhoneNumber <PhneNb> [0..1] Text 873
   MobileNumber <MobNb> [0..1] Text 873
   FaxNumber <FaxNb> [0..1] Text 873
   URLAddress <URLAdr> [0..1] Text 873
   EmailAddress <EmailAdr> [0..1] Text 873
   EmailPurpose <EmailPurp> [0..1] Text 873
   JobTitle <JobTitl> [0..1] Text 873
   Responsibility <Rspnsblty> [0..1] Text 873
   Department <Dept> [0..1] Text 874
   Other <Othr> [0..*]  874
     ChannelType <ChanlTp> [1..1] Text 874
     Identification <Id> [0..1] Text 874
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 874
6.1.17 Payment Type
6.1.17.1  PaymentTypeInformation27
Definition: Provides further details of the type of payment.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
868 March 2026
```

