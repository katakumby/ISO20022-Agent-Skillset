---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
preceding_topic_continuations: [{"constraint_ids": ["C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25"], "until_heading": "5.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 413, "topic": "5.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000174/sections/section-00289.md"}]
---

# 5.4 Message Building Blocks

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 413, C15–C25 before **5.4 Message Building Blocks** continue [5.3 Constraints](section-00289.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 413

```text
C15 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C16 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C17 PaymentTypeInformationRule
If PaymentTypeInformation is present, then DirectDebitTransactionInformation/
PaymentTypeInformation is not allowed.
C18 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C19 ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
C20 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C21 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C22 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C23 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C24 UltimateCreditorRule
If UltimateCreditor is present, then DirectDebitTransactionInformation/UltimateCreditor is not
allowed.
If DirectDebitTransactionInformation/UltimateCreditor is present, then UltimateCreditor is not
allowed.
DirectDebitTransactionInformation/UltimateCreditor and UltimateCreditor may both be absent.
C25 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 413 March 2026
```

