---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.2 Message Datatypes", "4.2.2 CodeSet", "4.2.2.5 CreditDebitCode"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.2.5 CreditDebitCode

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.2.2.5  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.2.2.6  ExternalAccountIdentification1Code
Definition: Specifies the external account identification scheme name code in the format of character
string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
4.2.2.7  ExternalEnquiryRequestType1Code
Definition: Specifies the external request type code for the enquiry on a position in the format of
character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
4.2.2.8  ExternalMarketInfrastructure1Code
Definition: Specifies the market infrastructure identification, as published in an external market
infrastructure code list.
This is a synonym of the external cash clearing system code list, extended outside the pure cash
domains.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 145 December 2025
```

