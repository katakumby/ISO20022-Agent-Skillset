---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.27 InstructionCopy <InstrCpy>"]
file_pages: [521]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.27 InstructionCopy <InstrCpy>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 521 to 521.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 521

```text
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.2.15.18.2.27  InstructionCopy <InstrCpy>
Presence: [0..1]
Definition: Copy of the original instruction, in free form text.
Usage: When the instruction being copied is an ISO 20022 message using the XML syntax a CDATA
format must be used.
Datatype: "Max20000Text" on page 915
3.4.2.15.18.2.28  AdditionalTransactionInformation <AddtlTxInf>
Presence: [0..1]
Definition: Further details of the transaction.
Datatype: "Max500Text" on page 917
3.4.2.15.18.2.29  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C30 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 850 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 851
   Envelope <Envlp> [1..1] (External Schema) 851
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4.2.15.19  AdditionalEntryInformation <AddtlNtryInf>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
521 March 2026
```

