---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.6 SupplementaryData1", "6.1.15.6.1 PlaceAndName <PlcAndNm>"]
file_pages: [851]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.6.1 PlaceAndName <PlcAndNm>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 851 to 851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 851

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
6.1.15.6.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 916
6.1.15.6.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
6.1.15.7  Purpose2Choice
Definition: Specifies the underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 851
Or}   Proprietary <Prtry> [1..1] Text 851
6.1.15.7.1  Code <Cd>
Presence: [1..1]
Definition: Underlying reason for the payment transaction, as published in an external purpose code list.
Datatype: "ExternalPurpose1Code" on page 899
6.1.15.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Purpose, in a proprietary form.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
851 March 2026
```

