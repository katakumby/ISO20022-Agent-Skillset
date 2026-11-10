---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.3 RequestedAdviceType <ReqdAdvcTp>", "2.4.2.3.1 CreditAdvice <CdtAdvc>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.3.1 CreditAdvice <CdtAdvc>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
RequestedAdviceType <ReqdAdvcTp> contains the following AdviceType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditAdvice <CdtAdvc> [0..1]  34
{Or     Code <Cd> [1..1] CodeSet 34
Or}     Proprietary <Prtry> [1..1] Text 34
   DebitAdvice <DbtAdvc> [0..1]  34
{Or     Code <Cd> [1..1] CodeSet 35
Or}     Proprietary <Prtry> [1..1] Text 35
2.4.2.3.1  CreditAdvice <CdtAdvc>
Presence: [0..1]
Definition: Type of credit advice requested.
CreditAdvice <CdtAdvc> contains one of the following AdviceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 34
Or}   Proprietary <Prtry> [1..1] Text 34
2.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Advice type, in a coded form.
Datatype: "AdviceType1Code" on page 587
CodeName Name Definition
ADWD AdviceWithDetails Advice with transaction details is
requested.
ADND AdviceWithoutDetails Advice without transaction details is
requested.
2.4.2.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Advice type, in a proprietary form.
Datatype: "Max35Text" on page 609
2.4.2.3.2  DebitAdvice <DbtAdvc>
Presence: [0..1]
Definition: Type de debit advice requested.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 34 March 2026
```

