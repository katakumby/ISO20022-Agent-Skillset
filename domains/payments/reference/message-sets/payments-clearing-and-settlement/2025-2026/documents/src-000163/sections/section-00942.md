---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.3 CodeSet", "10.2.3.46 SequenceType3Code"]
file_pages: [1237]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.3.46 SequenceType3Code

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1237 to 1237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1237

```text
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
EDIC ElectronicDataInterchange Remittance advice information must be
sent through Electronic Data Interchange
(EDI).
URID UniformResourceIdentifier Remittance advice information needs to
be sent to a Uniform Resource Identifier
(URI). URI is a compact string of
characters that uniquely identify an
abstract or physical resource. URI's are
the super-set of identifiers, such as
URLs, email addresses, ftp sites, etc,
and as such, provide the syntax for all of
the identification schemes.
EMAL EMail Remittance advice information must be
sent through e-mail.
POST Post Remittance advice information must be
sent through postal services.
SMSM SMS Remittance advice information must be
sent through by phone as a short
message service (SMS).
10.2.3.46  SequenceType3Code
Definition: Specifies the type of the current transaction that belongs to a sequence of transactions.
Type: CodeSet
CodeName Name Definition
FRST First First collection of a series of direct debit
instructions.
RCUR Recurring Direct debit instruction where the
debtor's authorisation is used for regular
direct debit transactions initiated by the
creditor.
FNAL Final Final collection of a series of direct debit
instructions.
OOFF OneOff Direct debit instruction where the
debtor's authorisation is used to initiate
one single direct debit transaction.
RPRE Represented Collection used to re-present previously
reversed or returned direct debit
transactions.
10.2.3.47  SettlementMethod1Code
Definition: Specifies the method used to settle the credit transfer instruction.
Type: CodeSet
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1237 March 2026
```

