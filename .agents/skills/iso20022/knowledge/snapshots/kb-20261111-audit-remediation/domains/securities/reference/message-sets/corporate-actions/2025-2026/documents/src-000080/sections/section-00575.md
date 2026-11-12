---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>", "13.4.4.5 ProprietaryStatus <PrtrySts>"]
file_pages: [746, 747]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.4.5 ProprietaryStatus <PrtrySts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 746 to 747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 746

```text
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingCancellationStatus18Choice" on page 1150 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1151
Or}   Reason <Rsn> [1..*]  C5 1151
     ReasonCode <RsnCd> [1..1]  1151
{Or       Code <Cd> [1..1] CodeSet 1152
Or}       Proprietary <Prtry> [1..1] ± 1152
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1152
13.4.4.5  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary status related to an instruction cancellation request.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 1140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1141
   ProprietaryReason <PrtryRsn> [0..*] ± C2 1141
13.4.5 CorporateActionInstruction <CorpActnInstr>
Presence: [0..1]
Definition: Information about the corporate action option.
Impacted by: C20 "OptionNumberRule", C22 "SafekeepingAccountOrBlockChainAddress1Rule", C23
"SafekeepingAccountOrBlockChainAddress2Rule", C24
"SafekeepingAccountOrBlockChainAddress3Rule", C25 "SafekeepingPlaceRule", C27
"StatusQuantityOrStatusCashAmount1Rule", C28 "StatusQuantityOrStatusCashAmount2Rule"
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 746 February 2026
```

## File page 747

```text
CorporateActionInstruction <CorpActnInstr> contains the following CorporateActionOption239
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 748
   OptionType <OptnTp> [1..1] ± 748
   OptionFeatures <OptnFeatrs> [0..1] ± 748
   AccountOwner <AcctOwnr> [0..1] ± 749
   SafekeepingAccount <SfkpgAcct> [0..1] Text 749
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 749
   CashAccount <CshAcct> [0..1] ± 749
   SafekeepingPlace <SfkpgPlc> [0..1] ± 750
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C11,
C12,
C17,
C18,
C21
750
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 751
   InstructedBalance <InstdBal> [0..1] ± 752
   UninstructedBalance <UinstdBal> [0..1] ± 752
   ProtectBalance <PrtctBal> [0..1] ± 752
   StatusQuantity <StsQty> [0..1] ± 753
   StatusCashAmount <StsCshAmt> [0..1] Amount C1, C10 753
Constraints
• OptionNumberRule
For differentiation between options, the OptionNumber rather than the OptionType must be used, for
example, in the case where two or more offers can be described by the same corporate action option
code. Therefore, the OptionNumber value must be different for each option.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 747 February 2026
```

